# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Camera.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Camera_Window(object):
    def setupUi(self, Camera_Window):
        Camera_Window.setObjectName("Camera_Window")
        Camera_Window.resize(899, 630)
        Camera_Window.setStyleSheet("background-color: rgb(26, 26, 26);")
        self.centralwidget = QtWidgets.QWidget(Camera_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 30, 741, 451))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setStyleSheet("QLabel{\n"
"    border: 5px solid rgb(38, 38, 48);\n"
"    border-radius: 20px;\n"
"    color: #FFF;\n"
"    padding-left: 15px;\n"
"    background-color: rgb(32, 32, 32);\n"
"}")
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalSlider = QtWidgets.QSlider(self.layoutWidget)
        self.verticalSlider.setStyleSheet("QVerticalSlider{\n"
"    border: 5px solid rgb(38, 38, 48);\n"
"    border-radius: 20px;\n"
"    color: #FFF;\n"
"    padding-left: 15px;\n"
"    background-color: rgb(32, 32, 32);\n"
"\n"
"}")
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.horizontalLayout.addWidget(self.verticalSlider)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 2)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 490, 131, 41))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    border-radius:15px;\n"
"\n"
"    \n"
"    background-color: rgb(30, 200, 200);\n"
"\n"
"    color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(30, 150, 150);\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 490, 131, 41))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    border-radius:15px;\n"
"\n"
"    \n"
"    background-color: rgb(30, 200, 200);\n"
"\n"
"    color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(30, 150, 150);\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        Camera_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Camera_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 899, 26))
        self.menubar.setObjectName("menubar")
        Camera_Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Camera_Window)
        self.statusbar.setObjectName("statusbar")
        Camera_Window.setStatusBar(self.statusbar)

        self.retranslateUi(Camera_Window)
        QtCore.QMetaObject.connectSlotsByName(Camera_Window)

    def retranslateUi(self, Camera_Window):
        _translate = QtCore.QCoreApplication.translate
        Camera_Window.setWindowTitle(_translate("Camera_Window", "MainWindow"))
        self.pushButton_2.setText(_translate("Camera_Window", "Open"))
        self.pushButton.setText(_translate("Camera_Window", "Save"))

