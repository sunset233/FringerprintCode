
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QLabel, QDesktopWidget


class ImageWindow(QWidget):
    def __init__(self):
        super(ImageWindow,self).__init__()


        self.imagelabel = QLabel()
        self.imagelabel.resize(500,400)

    def center(self):
        # 获取屏幕坐标系和窗口坐标系
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        newLelt = (screen.width() -size.width()) / 2
        newTop = (screen.height() - size.height()) / 2
        self.move(newLelt,newTop)
