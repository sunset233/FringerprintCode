# --coding:utf-8--
# 定义层
import sys
import argparse
import numpy as np
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.applications.densenet import preprocess_input

target_size = (224, 224)


# 预测函数
# 输入：model，图片，目标尺寸
# 输出：预测predict
def predict(model, img, target_size):
    """Run model prediction on image
    Args:
      model: keras model
      img: PIL format image
      target_size: (w,h) tuple
    Returns:
      list of predicted labels and their probabilities
    """
    if img.size != target_size:
        img = img.resize(target_size)

    x = tf.keras.preprocessing.image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = model.predict(x)
    return preds


# 画图函数

tuple = ("chenjack9", "guojingfei8", "hanmeim2", "huangfh4", "liuhuafeng4",
          "simphson5", "smithjudy10", "tommyli6", "zhangwx7", "zhaoyun3")

labels = {"chenjack9":"陈杰明", "guojingfei8":"郭京飞", "hanmeim2":"韩梅梅", "huangfh4":"黄飞鸿", "liuhuafeng4":"刘华峰",
          "simphson5":"辛普森", "smithjudy10":"朱迪", "tommyli6":"拖米", "zhangwx7":"张伟欣", "zhaoyun3":"赵云"}
def getResult(img_path):
    # 载入模型
    model = tf.keras.models.load_model('D:/python program/NIST_Training/model.h5')

    # 本地图片进行预测
    img = Image.open(img_path)
    preds = predict(model, img, target_size)
    preds = tf.nn.softmax(preds)
    print(preds)
    list = preds.numpy().tolist()
    i = 0
    max = -1
    for item in list[0]:
        if max < item:
            label = i
            max = item
        i = i + 1
    print(labels[tuple[label]])

    return labels[tuple[label]]

if __name__ == '__main__':
    getResult('D:/python program/NIST_Training/test/1-11.jpg')#赵云 赵云
    getResult('D:/python program/NIST_Training/test/2-3.jpg') #韩梅梅 赵云
    getResult('D:/python program/NIST_Training/test/3-23.jpg')#黄飞鸿 黄飞鸿
    getResult('D:/python program/NIST_Training/test/4-8.jpg') #拖米 辛普森
    getResult('D:/python program/NIST_Training/test/5-16.jpg')#黄飞鸿 辛普森
    getResult('D:/python program/NIST_Training/test/6-5.jpg') #拖米 黄飞鸿
    getResult('D:/python program/NIST_Training/test/7-23.jpg')#韩梅梅 韩梅梅
    getResult('D:/python program/NIST_Training/test/8-18.jpg')#韩梅梅 韩梅梅
    getResult('D:/python program/NIST_Training/test/9-3.jpg') #拖米 辛普森
    getResult('D:/python program/NIST_Training/test/10-16.jpg')#黄飞鸿 辛普森
