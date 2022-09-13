# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Giris.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Giris_Window(object):
    def setupUi(self, Giris_Window):
        Giris_Window.setObjectName("Giris_Window")
        Giris_Window.resize(350, 264)
        Giris_Window.setStyleSheet("background-color: rgb(26, 26, 26);")
        self.centralwidget = QtWidgets.QWidget(Giris_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.Giris_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.Giris_pushButton.setGeometry(QtCore.QRect(40, 170, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Giris_pushButton.setFont(font)
        self.Giris_pushButton.setStyleSheet("QPushButton {\n"
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
        self.Giris_pushButton.setObjectName("Giris_pushButton")
        self.Kullaniciadi_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.Kullaniciadi_lineEdit.setGeometry(QtCore.QRect(40, 50, 271, 41))
        self.Kullaniciadi_lineEdit.setStyleSheet("QLineEdit{\n"
"    border: 5px solid rgb(38, 38, 48);\n"
"    border-radius: 20px;\n"
"    color: #FFF;\n"
"    padding-left: 15px;\n"
"    background-color: rgb(32, 32, 32);\n"
"\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(48, 50, 62)\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(35, 218, 233);\n"
"}")
        self.Kullaniciadi_lineEdit.setText("")
        self.Kullaniciadi_lineEdit.setObjectName("Kullaniciadi_lineEdit")
        self.Sifre_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.Sifre_lineEdit.setGeometry(QtCore.QRect(40, 110, 271, 41))
        self.Sifre_lineEdit.setStyleSheet("QLineEdit{\n"
"    border: 5px solid rgb(38, 38, 48);\n"
"    border-radius: 20px;\n"
"    color: #FFF;\n"
"    padding-left: 15px;\n"
"    background-color: rgb(32, 32, 32);\n"
"\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(48, 50, 62)\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(35, 218, 233);\n"
"}")
        self.Sifre_lineEdit.setText("")
        self.Sifre_lineEdit.setObjectName("Sifre_lineEdit")
        Giris_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Giris_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 350, 26))
        self.menubar.setObjectName("menubar")
        Giris_Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Giris_Window)
        self.statusbar.setObjectName("statusbar")
        Giris_Window.setStatusBar(self.statusbar)

        self.retranslateUi(Giris_Window)
        QtCore.QMetaObject.connectSlotsByName(Giris_Window)

    def retranslateUi(self, Giris_Window):
        _translate = QtCore.QCoreApplication.translate
        Giris_Window.setWindowTitle(_translate("Giris_Window", "MainWindow"))
        self.Giris_pushButton.setText(_translate("Giris_Window", "Giriş"))
        self.Kullaniciadi_lineEdit.setPlaceholderText(_translate("Giris_Window", "   Kullanıcı Adı"))
        self.Sifre_lineEdit.setPlaceholderText(_translate("Giris_Window", "   Şifre"))

