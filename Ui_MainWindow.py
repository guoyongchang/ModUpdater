# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\ModUpdater\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
class ModUpdater(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
    #重写三个方法使我们的Example窗口支持拖动,上面参数window就是拖动对象
    def mousePressEvent(self, event):
        if event.button()==Qt.LeftButton:
            self.m_drag=True
            self.m_DragPosition=event.globalPos()-self.pos()
            event.accept()
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_drag:
            self.move(QMouseEvent.globalPos()-self.m_DragPosition)
            QMouseEvent.accept()
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag=False
        
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 150)
        MainWindow.setStyleSheet("background-color: rgb(92, 73, 120);")
        #打开后定位
        MainWindow.m_DragPosition=MainWindow.pos()
        #设置无边框
        MainWindow.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        #设置可拖拽
        MainWindow.setMouseTracking(True)
        
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.pushButton_Close = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_Close.setGeometry(QtCore.QRect(275, 0, 25, 25))
        self.pushButton_Close.setAutoFillBackground(False)
        self.pushButton_Close.setStyleSheet("color: rgb(245, 5, 5);\n"
"font-weight:bold;\n"
"font-size:18px;\n"
"border:none;")
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
        self.progressBar.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 0, 0, 255), stop:0.339795 rgba(255, 0, 0, 255), stop:0.339799 rgba(255, 255, 255, 255), stop:0.662444 rgba(255, 255, 255, 255), stop:0.662469 rgba(0, 0, 255, 255), stop:1 rgba(0, 0, 255, 255));")
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
        self.pushButton_Close.clicked.connect(MainWindow.close)
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
    MainWindow = ModUpdater()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

