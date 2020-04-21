# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog

from Classifer import getResult


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(505, 340)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setGeometry(QtCore.QRect(20, 50, 75, 23))
        self.button1.setObjectName("button1")
        self.button1.clicked.connect(self.ShowImage())
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 260, 75, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 505, 23))
        self.menubar.setObjectName("menubar")
        self.File = QtWidgets.QMenu(self.menubar)
        self.File.setObjectName("File")
        self.Search = QtWidgets.QMenu(self.menubar)
        self.Search.setObjectName("Search")
        self.Help = QtWidgets.QMenu(self.menubar)
        self.Help.setObjectName("Help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.process = QtWidgets.QAction(MainWindow)
        self.process.setObjectName("process")
        self.exit = QtWidgets.QAction(MainWindow)
        self.exit.setObjectName("exit")
        self.exit.triggered.connect(self.Exiting)
        self.model = QtWidgets.QAction(MainWindow)
        self.model.setObjectName("model")
        self.training = QtWidgets.QAction(MainWindow)
        self.training.setObjectName("training")
        self.guide = QtWidgets.QAction(MainWindow)
        self.guide.setObjectName("guide")
        self.result = QtWidgets.QAction(MainWindow)
        self.result.setObjectName("result")
        self.contact = QtWidgets.QAction(MainWindow)
        self.contact.setObjectName("contact")
        self.File.addAction(self.process)
        self.File.addAction(self.exit)
        self.Search.addAction(self.model)
        self.Search.addAction(self.training)
        self.Search.addAction(self.result)
        self.Help.addAction(self.guide)
        self.Help.addAction(self.contact)
        self.menubar.addAction(self.File.menuAction())
        self.menubar.addAction(self.Search.menuAction())
        self.menubar.addAction(self.Help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "指纹识别系统"))
        self.button1.setText(_translate("MainWindow", "加载图片"))
        self.pushButton.setText(_translate("MainWindow", "确定"))
        self.File.setTitle(_translate("MainWindow", "文件"))
        self.Search.setTitle(_translate("MainWindow", "查看"))
        self.Help.setTitle(_translate("MainWindow", "帮助"))
        self.process.setText(_translate("MainWindow", "模型流程"))
        self.exit.setText(_translate("MainWindow", "退出"))
        self.model.setText(_translate("MainWindow", "模型参数"))
        self.training.setText(_translate("MainWindow", "模型训练参数"))
        self.guide.setText(_translate("MainWindow", "使用说明"))
        self.result.setText(_translate("MainWindow", "模型训练结果"))
        self.contact.setText(_translate("MainWindow", "联系我们"))

    def ShowImage(self):
        fname, _ = QFileDialog.getOpenFileName(self, '打开图片', '.', '图像文件(*.jpg *.png)')
        self.imageLabel.setPixmap(QPixmap(fname))
        getResult(fname)

    def Exiting(self):
        self.close()