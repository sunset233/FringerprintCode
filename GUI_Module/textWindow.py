import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

class TextWindow(QWidget):
    def __init__(self):
        super(TextWindow,self).__init__()
        #layout = QVBoxLayout()


        self.textlabel = QTextBrowser()



    def center(self):
        # 获取屏幕坐标系和窗口坐标系
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        newLelt = (screen.width() -size.width()) / 2
        newTop = (screen.height() - size.height()) / 2
        self.move(newLelt,newTop)
