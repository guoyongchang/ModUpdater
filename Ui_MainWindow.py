# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\ModUpdater\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    #支持窗口拖动,重写两个方法
    def mousePressEvent(self, event):
        if event.button()==QtWidgets.LeftButton:
            self.m_drag=True
            self.m_DragPosition=event.globalPos()-self.pos()
            event.accept()
 
    def mouseMoveEvent(self, QMouseEvent):
        if QMouseEvent.buttons() and QtWidgets.LeftButton:
            self.move(QMouseEvent.globalPos()-self.m_DragPosition)
            QMouseEvent.accept()
 
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag=False
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 150)
        MainWindow.setStyleSheet("background-color: rgb(92, 73, 120);")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        #打开后定位
        MainWindow.m_DragPosition=MainWindow.pos()
        #设置无边框
        MainWindow.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        #设置可拖拽
        MainWindow.setMouseTracking(True)
        
        self.pushButton_Close = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_Close.setGeometry(QtCore.QRect(275, 0, 25, 25))
        self.pushButton_Close.setAutoFillBackground(False)
        self.pushButton_Close.setStyleSheet("color: rgb(245, 5, 5);""font-weight:bold;""font-size:18px;""border:none;")
        self.pushButton_Close.setObjectName("pushButton_Close")
        self.widget_Content = QtWidgets.QWidget(self.centralWidget)
        self.widget_Content.setGeometry(QtCore.QRect(0, 25, 300, 125))
        self.widget_Content.setStyleSheet("background-color: rgb(59, 71, 94);")
        self.widget_Content.setObjectName("widget_Content")
        self.lable_NowVersion_Read = QtWidgets.QLabel(self.widget_Content)
        self.lable_NowVersion_Read.setGeometry(QtCore.QRect(20, 10, 60, 12))
        self.lable_NowVersion_Read.setStyleSheet("color:#98FB98;")
        self.lable_NowVersion_Read.setObjectName("lable_NowVersion_Read")
        self.lable_NewVersion_Read = QtWidgets.QLabel(self.widget_Content)
        self.lable_NewVersion_Read.setGeometry(QtCore.QRect(20, 40, 60, 12))
        self.lable_NewVersion_Read.setStyleSheet("color:#98FB98;")
        self.lable_NewVersion_Read.setObjectName("lable_NewVersion_Read")
        self.lable_NowVersion = QtWidgets.QLabel(self.widget_Content)
        self.lable_NowVersion.setGeometry(QtCore.QRect(80, 10, 210, 12))
        self.lable_NowVersion.setStyleSheet("color:#98FB98;")
        self.lable_NowVersion.setObjectName("lable_NowVersion")
        self.lable_NewVersion = QtWidgets.QLabel(self.widget_Content)
        self.lable_NewVersion.setGeometry(QtCore.QRect(80, 40, 210, 12))
        self.lable_NewVersion.setStyleSheet("color:#98FB98;")
        self.lable_NewVersion.setObjectName("lable_NewVersion")
        self.progressBar = QtWidgets.QProgressBar(self.widget_Content)
        self.progressBar.setGeometry(QtCore.QRect(20, 90, 260, 30))
        self.progressBar.setProperty("value", 100)
        self.progressBar.setTextVisible(False)
        self.progressBar.setFormat("")
        self.progressBar.setObjectName("progressBar")
        self.pushButton = QtWidgets.QPushButton(self.widget_Content)
        self.pushButton.setGeometry(QtCore.QRect(200, 55, 80, 30))
        self.pushButton.setStyleSheet("background-color: rgb(229, 241, 251);")
        self.pushButton.setObjectName("pushButton")
        self.lable_NowEvent = QtWidgets.QLabel(self.widget_Content)
        self.lable_NowEvent.setGeometry(QtCore.QRect(20, 70, 170, 12))
        self.lable_NowEvent.setStyleSheet("color:#98FB98;")
        self.lable_NowEvent.setObjectName("lable_NowEvent")
        self.label_Title = QtWidgets.QLabel(self.centralWidget)
        self.label_Title.setGeometry(QtCore.QRect(0, 0, 275, 25))
        self.label_Title.setStyleSheet("color:#FF8C00;")
        self.label_Title.setTextFormat(QtCore.Qt.AutoText)
        self.label_Title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Title.setObjectName("label_Title")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        #self.pushButton_Close.clicked.connect(self.pushButton_Close.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_Close.setText(_translate("MainWindow", "×"))
        self.lable_NowVersion_Read.setText(_translate("MainWindow", "当前版本:"))
        self.lable_NewVersion_Read.setText(_translate("MainWindow", "最新版本:"))
        self.lable_NowVersion.setText(_translate("MainWindow", "TextLabel"))
        self.lable_NewVersion.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton.setText(_translate("MainWindow", "更新|修复"))
        self.lable_NowEvent.setText(_translate("MainWindow", "TextLabel"))
        self.label_Title.setText(_translate("MainWindow", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

