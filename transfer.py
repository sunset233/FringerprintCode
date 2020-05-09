import  matplotlib
from    matplotlib import pyplot as plt



matplotlib.rcParams['font.size'] = 18
matplotlib.rcParams['figure.titlesize'] = 18
matplotlib.rcParams['figure.figsize'] = [9, 7]
matplotlib.rcParams['font.family'] = ['KaiTi']
matplotlib.rcParams['axes.unicode_minus']=False

import  os
import  tensorflow as tf
import  numpy as np
from    tensorflow import keras
from    tensorflow.keras import layers,optimizers,losses
from    tensorflow.keras.callbacks import EarlyStopping

tf.random.set_seed(1234)
np.random.seed(1234)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
assert tf.__version__.startswith('2.')


from data_loading import  load_nist,normalize



def preprocess(x,y):
    # x: 图片的路径，y：图片的数字编码
    x = tf.io.read_file(x)
    x = tf.image.decode_jpeg(x, channels=3) # RGBA
    x = tf.image.resize(x, [244, 244])

    x = tf.image.random_flip_left_right(x)
    x = tf.image.random_flip_up_down(x)
    x = tf.image.random_crop(x, [224,224,3])

    # x: [0,255]=> -1~1
    x = tf.cast(x, dtype=tf.float32) / 255.
    x = normalize(x)
    y = tf.convert_to_tensor(y)
    y = tf.one_hot(y, depth=10)

    return x, y


batchsz = 32
# 创建训练集Datset对象
images, labels, table = load_nist('nist',mode='train')
db_train = tf.data.Dataset.from_tensor_slices((images, labels))
db_train = db_train.shuffle(1000).map(preprocess).batch(batchsz)

# 加载DenseNet网络模型，并去掉最后一层全连接层，最后一个池化层设置为max pooling

net = tf.keras.applications.DenseNet169(weights = 'imagenet', include_top=False, pooling='max')

# 设计为不参与优化，即MobileNet这部分参数固定不动
net.trainable = False
newnet = keras.Sequential([
    net, # 去掉最后一层的DenseNet121
    layers.Dense(1024, activation='relu'), # 追加全连接层
    layers.BatchNormalization(), # 追加BN层
    layers.Dropout(rate=0.5), # 追加Dropout层，防止过拟合
    layers.Dense(10) # 根据指纹数据集，设置最后一层输出节点数为10， 用来表示指纹的类别数
])
newnet.build(input_shape=(4,224,224,3))
newnet.summary()

# 创建Early Stopping类，连续3次不下降则终止
early_stopping = EarlyStopping(
    monitor='accuracy',
    min_delta=0.0001,
    patience=3
)

newnet.compile(optimizer=optimizers.Adam(lr=1e-3),
               loss=losses.CategoricalCrossentropy(from_logits=True),
               metrics=['accuracy'])
history  = newnet.fit(db_train, epochs=100,
           callbacks=[early_stopping])
newnet.save('model.h5')
history = history.history
print(history.keys())
print(history['accuracy'])




plt.figure()
returns = history['accuracy']
plt.plot(np.arange(len(returns)), returns, label='训练准确率')
plt.plot(np.arange(len(returns)), returns, 's')

plt.legend()
plt.xlabel('Epoch')
plt.ylabel('准确率')
plt.savefig('scratch.svg')