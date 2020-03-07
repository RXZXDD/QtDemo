# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TCP.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labCamera = QtWidgets.QLabel(self.centralwidget)
        self.labCamera.setMinimumSize(QtCore.QSize(640, 480))
        self.labCamera.setObjectName("labCamera")
        self.verticalLayout.addWidget(self.labCamera)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labPort = QtWidgets.QLabel(self.centralwidget)
        self.labPort.setObjectName("labPort")
        self.horizontalLayout.addWidget(self.labPort)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.btnListen = QtWidgets.QPushButton(self.centralwidget)
        self.btnListen.setObjectName("btnListen")
        self.horizontalLayout.addWidget(self.btnListen)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labCamera.setText(_translate("MainWindow", "TextLabel"))
        self.labPort.setText(_translate("MainWindow", "Port:"))
        self.lineEdit.setText(_translate("MainWindow", "9000"))
        self.btnListen.setText(_translate("MainWindow", "Listen"))
