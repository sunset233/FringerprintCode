import sys, math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Classifer import *
from GUI_Module.ImageWindow import ImageWindow

from GUI_Module.textWindow import TextWindow


class MainWindow(QMainWindow):
    fname = None

    def __init__(self):
        super(MainWindow,self).__init__()

        self.setWindowTitle('指纹识别系统')
        self.resize(600,400)
        self.move(50,100)

        bar = self.menuBar()
        file = bar.addMenu('文件')
        search = bar.addMenu('查看')
        help = bar.addMenu('帮助')

        # 退出菜单功能
        exit = QAction('退出', self)
        #exit.setShortcut('Ctrl + A')
        file.addAction(exit)
        exit.triggered.connect(self.Exiting)

        # 查看模型数据功能
        model = QAction('查看模型', self)
        search.addAction(model)
        model.triggered.connect(self.ModelInfo)
        training = QAction('查看模型训练',self)
        search.addAction(training)
        training.triggered.connect(self.TrainingInfo)
        result = QAction('查看模型结果',self)
        search.addAction(result)
        result.triggered.connect(self.TrainingResult)

        # 帮助菜单栏功能
        instruction = QAction('使用说明',self)
        help.addAction(instruction)
        instruction.triggered.connect(self.Helpme)
        contact = QAction('联系我们',self)
        help.addAction(contact)
        contact.triggered.connect(self.Contactus)
        about = QAction('关于',self)
        help.addAction(about)
        about.triggered.connect(self.About)

        self.button1 = QPushButton('加载图片',self)
        self.button1.move(20, 150)
        self.button1.clicked.connect(self.ShowImage)
        self.imageLabel = QLabel(self)
        self.imageLabel.resize(200,250)
        self.imageLabel.move(200, 50)
        self.button2 = QPushButton('开始识别',self)
        self.button2.move(210,350)
        self.button2.clicked.connect(self.Recognize)


    def ShowImage(self):
        fname, _ = QFileDialog.getOpenFileName(self, '打开图片', '.', '图像文件(*.jpg *.png)')
        self.fname = fname
        pixmap = QPixmap(fname)
        self.imageLabel.setPixmap(pixmap)
        self.imageLabel.setScaledContents(True)
        self.imageLabel.setPixmap(QPixmap(pixmap))

    def ModelInfo(self):
        model_path = 'model_data/model.txt'
        self.window = TextWindow()
        f = open(model_path, encoding='utf-8', mode='r')
        with f:
            data = f.read()
            self.window.textlabel.setText(data)
        self.window.textlabel.resize(500, 280)
        self.window.textlabel.setWindowTitle('模型展示')
        self.window.textlabel.show()

    def  TrainingResult(self):
        img_path = 'model_data/model.svg'
        self.img_show = ImageWindow()
        pixmap = QPixmap(img_path)
        self.img_show.imagelabel.setPixmap(pixmap)
        self.img_show.imagelabel.setWindowTitle('模型训练结果')
        self.img_show.imagelabel.setScaledContents(True)
        self.img_show.imagelabel.setPixmap(QPixmap(pixmap))
        self.img_show.imagelabel.show()

    def Recognize(self):
        name = getResult(self.fname)
        reply = QMessageBox.information(self, '验证结果', '指纹属于' + name + '的', QMessageBox.Yes | QMessageBox.No)
        print(reply == QMessageBox.Yes)


    def TrainingInfo(self):
        training_path = 'model_data/training_data.txt'
        self.window = TextWindow()
        f = open(training_path, encoding='utf-8', mode='r')
        with f:
            data = f.read()
            self.window.textlabel.setText(data)
        self.window.textlabel.setWindowTitle('训练数据展示')
        self.window.textlabel.resize(1000, 400)
        self.window.textlabel.show()
    def Exiting(self):
        self.close()

    def center(self):
        # 获取屏幕坐标系和窗口坐标系
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        newLelt = (screen.width() -size.width()) / 2
        newTop = (screen.height() - size.height()) / 2
        self.move(newLelt,newTop)

    def Contactus(self):
        QMessageBox.about(self,'联系我们','Email:123456789@qq.com')

    def Helpme(self):
        instruction = 'model_data/instruction.txt'
        self.window = TextWindow()
        f = open(instruction, encoding='utf-8', mode='r')
        with f:
            data = f.read()
            self.window.textlabel.setText(data)
        self.window.textlabel.setWindowTitle('使用说明')
        self.window.textlabel.resize(500, 200)
        self.window.textlabel.show()

    def About(self):
        QMessageBox.about(self,'关于','软件版本号：0.0.1')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('finger.ico'))
    main = MainWindow()
    main.center()
    main.show()
    sys.exit(app.exec_())