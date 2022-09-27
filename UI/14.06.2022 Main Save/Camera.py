# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Camera.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Camera_Window(object):
    def setupUi(self, Camera_Window):
        self.logic_All=0 ##""" Bütün Kameraların kapatılma sinyali"""
        self.Cam_I_Record=0 ##"""III. Kamera Kayıt sinyali"""
        self.Cam_I_Record_isOpen=0 ## I. Kamera Açık mı?
        self.Cam_II_Record=0 ##"""III. Kamera Kayıt sinyali"""
        
        self.Cam_III_Record=0 ##"""III. Kamera Kayıt sinyali"""
        self.Cam_III_Record_isOpen=0 ## III. Kamera Açık mı?
        
        self.Cam_IV_Record=0 ##"""III. Kamera Kayıt sinyali"""
        
        ########################################################
        #Kayıt Record
        self.count = 0
        self.text=0
        self.flag = False
        ########################################################
        
        ########################################################
        #Save Pic
        self.Cam_I_Save=0
        self.Cam_II_Save=0
        self.Cam_III_Save=0
        self.Cam_IV_Save=0
        
        ########################################################
    
    
    
    
        Camera_Window.setObjectName("Camera_Window")
        Camera_Window.resize(2000, 1000)
        Camera_Window.setStyleSheet("background-color: rgb(26, 26, 26);\n"
"QMenuBar {\n"
"  background-color: #455364;\n"
"  padding: 2px;\n"
"  border: 1px solid #19232D;\n"
"  color: #E0E1E3;\n"
"  selection-background-color: #1A72BB;\n"
"}\n"
"\n"
"QMenuBar:focus {\n"
"  border: 1px solid #346792;\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"  background: transparent;\n"
"  padding: 4px;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"  padding: 4px;\n"
"  background: transparent;\n"
"  border: 0px solid #455364;\n"
"  background-color: #1A72BB;\n"
"}\n"
"\n"
"QMenuBar::item:pressed {\n"
"  padding: 4px;\n"
"  border: 0px solid #455364;\n"
"  background-color: #1A72BB;\n"
"  color: #E0E1E3;\n"
"  margin-bottom: 0px;\n"
"  padding-bottom: 0px;\n"
"}\n"
"\n"
"/* QMenu ------------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qmenu\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QMenu {\n"
"  border: 0px solid #455364;\n"
"  color: #E0E1E3;\n"
"  margin: 0px;\n"
"  background-color: #37414F;\n"
"  selection-background-color: #1A72BB;\n"
"}\n"
"\n"
"QMenu::separator {\n"
"  height: 1px;\n"
"  background-color: #60798B;\n"
"  color: #E0E1E3;\n"
"}\n"
"\n"
"QMenu::item {\n"
"  background-color: #37414F;\n"
"  padding: 4px 24px 4px 28px;\n"
"  /* Reserve space for selection border */\n"
"  border: 1px transparent #455364;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"  color: #E0E1E3;\n"
"  background-color: #1A72BB;\n"
"}\n"
"\n"
"QMenu::item:pressed {\n"
"  background-color: #1A72BB;\n"
"}\n"
"\n"
"QMenu::icon {\n"
"  padding-left: 10px;\n"
"  width: 14px;\n"
"  height: 14px;\n"
"}\n"
"\n"
"QMenu::indicator {\n"
"  padding-left: 8px;\n"
"  width: 12px;\n"
"  height: 12px;\n"
"  /* non-exclusive indicator = check box style indicator (see QActionGroup::setExclusive) */\n"
"  /* exclusive indicator = radio button style indicator (see QActionGroup::setExclusive) */\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(Camera_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 1021, 181))
        self.groupBox.setStyleSheet("QGroupBox  {\n"
"    border: 1px solid gray;\n"
"    border-color: #FF17365D;\n"
"    margin-top: 27px;\n"
"    font-size: 14px;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QGroupBox::title  {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 5px 8000px 5px 8000px;\n"
"    background-color: #FF17365D;\n"
"    color: rgb(255, 255, 255);\n"
"    border-top-left-radius: 15px;\n"
"    border-top-right-radius: 15px;\n"
"    padding: 5px 250px;\n"
"    background-color: #FF17365D;\n"
"}\n"
"")
        self.groupBox.setObjectName("groupBox")
        self.Stop_pushButton = QtWidgets.QPushButton(self.groupBox)
        self.Stop_pushButton.setGeometry(QtCore.QRect(490, 70, 130, 50))
        self.Stop_pushButton.setStyleSheet("QPushButton {\n"
"    color:white;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1,y2:1, stop: 1 rgb(0, 255, 255), stop: 0 rgb(26, 26, 26));\n"
"\n"
"    border-color: rgb(26, 26, 26);\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-radius:20px;\n"
"    font:18px;\n"
"    border: 5px solid rgb(38, 38, 48);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(30, 150, 150);\n"
"}\n"
"")
        self.Stop_pushButton.setObjectName("Stop_pushButton")
        self.Start_pushButton = QtWidgets.QPushButton(self.groupBox)
        self.Start_pushButton.setGeometry(QtCore.QRect(330, 70, 130, 50))
        self.Start_pushButton.setStyleSheet("QPushButton {\n"
"    color:white;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1,y2:1, stop: 1 rgb(0, 255, 255), stop: 0 rgb(26, 26, 26));\n"
"\n"
"    border-color: rgb(26, 26, 26);\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-radius:20px;\n"
"    font:18px;\n"
"    border: 5px solid rgb(38, 38, 48);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(30, 150, 150);\n"
"}\n"
"")
        self.Start_pushButton.setObjectName("Start_pushButton")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 75, 111, 37))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:white;")
        self.label_3.setObjectName("label_3")
        self.Off_pushButton = QtWidgets.QPushButton(self.groupBox)
        self.Off_pushButton.setGeometry(QtCore.QRect(650, 70, 130, 50))
        self.Off_pushButton.setStyleSheet("QPushButton {\n"
"    color:white;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1,y2:1, stop: 1 rgb(0, 255, 255), stop: 0 rgb(26, 26, 26));\n"
"\n"
"    border-color: rgb(26, 26, 26);\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-radius:20px;\n"
"    font:18px;\n"
"    border: 5px solid rgb(38, 38, 48);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(30, 150, 150);\n"
"}\n"
"")
        self.Off_pushButton.setObjectName("Off_pushButton")
        self.Camera_comboBox = QtWidgets.QComboBox(self.groupBox)
        self.Camera_comboBox.setGeometry(QtCore.QRect(130, 70, 170, 50))
        self.Camera_comboBox.setStyleSheet("QComboBox\n"
"{\n"
"\n"
"    color:white;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1,y2:1, stop: 1 rgb(0, 255, 255), stop: 0 rgb(26, 26, 26));\n"
"    border-color: rgb(26, 26, 26);\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-radius:20px;\n"
"    font:18px;\n"
"    border: 5px solid rgb(38, 38, 48);\n"
"    padding-left: 15px;\n"
"}\n"
"\n"
"QComboBox QListView\n"
"{\n"
"    border-style: none;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1,y2:1, stop: 1 rgb(30, 200, 200), stop: 0 rgb(26, 26, 26));\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    width: 20px;\n"
"    border: 1px;\n"
"    border-color:rgb(26, 26, 26);\n"
"    border-left-style:solid;\n"
"    border-top-style: none;\n"
"    border-bottom-style: none;\n"
"    border-right-style: none;\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"    width: 16px;\n"
"    height: 16px;\n"
"}")
        self.Camera_comboBox.setObjectName("Camera_comboBox")
        self.Camera_comboBox.addItem("")
        self.Camera_comboBox.addItem("")
        self.Camera_comboBox.addItem("")
        self.Camera_comboBox.addItem("")
        self.Close_pushButton = QtWidgets.QPushButton(self.groupBox)
        self.Close_pushButton.setGeometry(QtCore.QRect(810, 70, 130, 50))
        self.Close_pushButton.setStyleSheet("QPushButton {\n"
"    color:white;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1,y2:1, stop: 1 rgb(0, 255, 255), stop: 0 rgb(26, 26, 26));\n"
"\n"
"    border-color: rgb(26, 26, 26);\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-radius:20px;\n"
"    font:18px;\n"
"    border: 5px solid rgb(38, 38, 48);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(30, 150, 150);\n"
"}\n"
"")
        self.Close_pushButton.setObjectName("Close_pushButton")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(1050, 10, 841, 181))
        self.groupBox_2.setStyleSheet("QGroupBox  {\n"
"    border: 1px solid gray;\n"
"    border-color: #FF17365D;\n"
"    margin-top: 27px;\n"
"    font-size: 14px;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QGroupBox::title  {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 5px 8000px 5px 8000px;\n"
"    background-color: #FF17365D;\n"
"    color: rgb(255, 255, 255);\n"
"    border-top-left-radius: 15px;\n"
"    border-top-right-radius: 15px;\n"
"    padding: 5px 250px;\n"
"    background-color: #FF17365D;\n"
"}\n"
"")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(130, 100, 231, 37))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.Fps_label = QtWidgets.QLabel(self.groupBox_2)
        self.Fps_label.setGeometry(QtCore.QRect(30, 50, 61, 37))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Fps_label.setFont(font)
        self.Fps_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.Fps_label.setObjectName("Fps_label")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(30, 100, 61, 37))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(400, 50, 231, 37))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.Calisma_label = QtWidgets.QLabel(self.groupBox_2)
        self.Calisma_label.setGeometry(QtCore.QRect(130, 50, 231, 37))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Calisma_label.setFont(font)
        self.Calisma_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.Calisma_label.setObjectName("Calisma_label")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(400, 100, 231, 37))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.Durum_Cam = QtWidgets.QLabel(self.groupBox_2)
        self.Durum_Cam.setGeometry(QtCore.QRect(680, 100, 231, 37))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Durum_Cam.setFont(font)
        self.Durum_Cam.setStyleSheet("color: rgb(255, 255, 255);")
        self.Durum_Cam.setObjectName("Durum_Cam")
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        self.label_15.setGeometry(QtCore.QRect(680, 50, 231, 37))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_15.setObjectName("label_15")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 210, 350, 570))
        self.groupBox_3.setStyleSheet("QGroupBox  {\n"
"    border: 1px solid gray;\n"
"    border-color: #FF17365D;\n"
"    margin-top: 27px;\n"
"    font-size: 14px;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QGroupBox::title  {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 5px 8000px 5px 8000px;\n"
"    background-color: #FF17365D;\n"
"    color: rgb(255, 255, 255);\n"
"    border-top-left-radius: 15px;\n"
"    border-top-right-radius: 15px;\n"
"    padding: 5px 50px;\n"
"    background-color: #FF17365D;\n"
"}\n"
"")
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalSlider = QtWidgets.QSlider(self.groupBox_3)
        self.horizontalSlider.setGeometry(QtCore.QRect(119, 60, 211, 21))
        self.horizontalSlider.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: 1px solid #bbb;\n"
"    background-color: rgb(26, 26, 26);\n"
"    height: 20px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1,y2:1, stop: 1 rgb(30, 200, 200), stop: 0 rgb(26, 26, 26));\n"
"    background: qlineargradient(x1:0, y1:0, x2:1,y2:1, stop: 1 rgb(30, 200, 200), stop: 0 rgb(26, 26, 26));\n"
"    border: 1px solid #777;\n"
"    height: 10px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: #fff;\n"
"    border: 1px solid #777;\n"
"    height: 10px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #FF17365D, stop:1 #FF17365D);\n"
"    border: 1px solid #777;\n"
"    width: 13px;\n"
"    margin-top: -2px;\n"
"    margin-bottom: -2px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #FF17365D, stop:1 #FF17365D);\n"
"    border: 1px solid #444;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"    background: #bbb;\n"
"    border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"    background: #eee;\n"
"    border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"    background: #eee;\n"
"    border: 1px solid #aaa;\n"
"    border-radius: 4px;\n"
"}")
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(20, 50, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:white;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(21, 110, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:white;")
        self.label_5.setObjectName("label_5")
        self.horizontalSlider_2 = QtWidgets.QSlider(self.groupBox_3)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(120, 120, 211, 22))
        self.horizontalSlider_2.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: 1px solid #bbb;\n"
"    background-color: rgb(26, 26, 26);\n"
"    height: 20px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1,y2:1, stop: 1 rgb(30, 200, 200), stop: 0 rgb(26, 26, 26));\n"
"    background: qlineargradient(x1:0, y1:0, x2:1,y2:1, stop: 1 rgb(30, 200, 200), stop: 0 rgb(26, 26, 26));\n"
"    border: 1px solid #777;\n"
"    height: 10px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: #fff;\n"
"    border: 1px solid #777;\n"
"    height: 10px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #FF17365D, stop:1 #FF17365D);\n"
"    border: 1px solid #777;\n"
"    width: 13px;\n"
"    margin-top: -2px;\n"
"    margin-bottom: -2px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #FF17365D, stop:1 #FF17365D);\n"
"    border: 1px solid #444;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"    background: #bbb;\n"
"    border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"    background: #eee;\n"
"    border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"    background: #eee;\n"
"    border: 1px solid #aaa;\n"
"    border-radius: 4px;\n"
"}")
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(20, 170, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color:white;")
        self.label_12.setObjectName("label_12")
        self.horizontalSlider_3 = QtWidgets.QSlider(self.groupBox_3)
        self.horizontalSlider_3.setGeometry(QtCore.QRect(119, 180, 211, 22))
        self.horizontalSlider_3.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: 1px solid #bbb;\n"
"    background-color: rgb(26, 26, 26);\n"
"    height: 20px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1,y2:1, stop: 1 rgb(30, 200, 200), stop: 0 rgb(26, 26, 26));\n"
"    background: qlineargradient(x1:0, y1:0, x2:1,y2:1, stop: 1 rgb(30, 200, 200), stop: 0 rgb(26, 26, 26));\n"
"    border: 1px solid #777;\n"
"    height: 10px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: #fff;\n"
"    border: 1px solid #777;\n"
"    height: 10px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #FF17365D, stop:1 #FF17365D);\n"
"    border: 1px solid #777;\n"
"    width: 13px;\n"
"    margin-top: -2px;\n"
"    margin-bottom: -2px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #FF17365D, stop:1 #FF17365D);\n"
"    border: 1px solid #444;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"    background: #bbb;\n"
"    border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"    background: #eee;\n"
"    border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"    background: #eee;\n"
"    border: 1px solid #aaa;\n"
"    border-radius: 4px;\n"
"}")
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        self.label_13.setGeometry(QtCore.QRect(21, 230, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color:white;")
        self.label_13.setObjectName("label_13")
        self.horizontalSlider_4 = QtWidgets.QSlider(self.groupBox_3)
        self.horizontalSlider_4.setGeometry(QtCore.QRect(120, 240, 211, 22))
        self.horizontalSlider_4.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: 1px solid #bbb;\n"
"    background-color: rgb(26, 26, 26);\n"
"    height: 20px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1,y2:1, stop: 1 rgb(30, 200, 200), stop: 0 rgb(26, 26, 26));\n"
"    background: qlineargradient(x1:0, y1:0, x2:1,y2:1, stop: 1 rgb(30, 200, 200), stop: 0 rgb(26, 26, 26));\n"
"    border: 1px solid #777;\n"
"    height: 10px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: #fff;\n"
"    border: 1px solid #777;\n"
"    height: 10px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #FF17365D, stop:1 #FF17365D);\n"
"    border: 1px solid #777;\n"
"    width: 13px;\n"
"    margin-top: -2px;\n"
"    margin-bottom: -2px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #FF17365D, stop:1 #FF17365D);\n"
"    border: 1px solid #444;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"    background: #bbb;\n"
"    border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"    background: #eee;\n"
"    border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"    background: #eee;\n"
"    border: 1px solid #aaa;\n"
"    border-radius: 4px;\n"
"}")
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setObjectName("horizontalSlider_4")
        self.Ac_pushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.Ac_pushButton.setGeometry(QtCore.QRect(30, 500, 130, 50))
        self.Ac_pushButton.setStyleSheet("QPushButton {\n"
"    color:white;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1,y2:1, stop: 1 rgb(0, 255, 255), stop: 0 rgb(26, 26, 26));\n"
"\n"
"    border-color: rgb(26, 26, 26);\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-radius:20px;\n"
"    font:18px;\n"
"    border: 5px solid rgb(38, 38, 48);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(30, 150, 150);\n"
"}\n"
"")
        self.Ac_pushButton.setObjectName("Ac_pushButton")
        self.Kayit_pushButton_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.Kayit_pushButton_2.setGeometry(QtCore.QRect(180, 500, 130, 50))
        self.Kayit_pushButton_2.setStyleSheet("QPushButton {\n"
"    color:white;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1,y2:1, stop: 1 rgb(0, 255, 255), stop: 0 rgb(26, 26, 26));\n"
"\n"
"    border-color: rgb(26, 26, 26);\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-radius:20px;\n"
"    font:18px;\n"
"    border: 5px solid rgb(38, 38, 48);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(30, 150, 150);\n"
"}\n"
"")
        self.Kayit_pushButton_2.setObjectName("Kayit_pushButton_2")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(380, 210, 1511, 571))
        self.groupBox_4.setStyleSheet("QGroupBox  {\n"
"    border: 1px solid gray;\n"
"    border-color: #FF17365D;\n"
"    margin-top: 27px;\n"
"    font-size: 14px;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QGroupBox::title  {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 5px 8000px 5px 8000px;\n"
"    background-color: #FF17365D;\n"
"    color: rgb(255, 255, 255);\n"
"    border-top-left-radius: 15px;\n"
"    border-top-right-radius: 15px;\n"
"    padding: 5px 250px;\n"
"    background-color: #FF17365D;\n"
"}\n"
"")
        self.groupBox_4.setObjectName("groupBox_4")
        self.Camera_1 = QtWidgets.QLabel(self.groupBox_4)
        self.Camera_1.setGeometry(QtCore.QRect(20, 50, 700, 500))
        self.Camera_1.setStyleSheet("QLabel{\n"
"    border: 5px solid rgb(38, 38, 48);\n"
"    border-radius: 20px;\n"
"    color: #FFF;\n"
"    padding-left: 15px;\n"
"    background-color: rgb(32, 32, 32);\n"
"}")
        self.Camera_1.setText("")
        self.Camera_1.setObjectName("Camera_1")
        self.Camera_2 = QtWidgets.QLabel(self.groupBox_4)
        self.Camera_2.setGeometry(QtCore.QRect(770, 50, 700, 500))
        self.Camera_2.setStyleSheet("QLabel{\n"
"    border: 5px solid rgb(38, 38, 48);\n"
"    border-radius: 20px;\n"
"    color: #FFF;\n"
"    padding-left: 15px;\n"
"    background-color: rgb(32, 32, 32);\n"
"}")
        self.Camera_2.setText("")
        self.Camera_2.setObjectName("Camera_2")
        Camera_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Camera_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 2000, 26))
        self.menubar.setObjectName("menubar")
        self.menuAna_Sayfa = QtWidgets.QMenu(self.menubar)
        self.menuAna_Sayfa.setObjectName("menuAna_Sayfa")
        self.menuCamera = QtWidgets.QMenu(self.menubar)
        self.menuCamera.setObjectName("menuCamera")
        Camera_Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Camera_Window)
        self.statusbar.setObjectName("statusbar")
        Camera_Window.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuAna_Sayfa.menuAction())
        self.menubar.addAction(self.menuCamera.menuAction())

        self.retranslateUi(Camera_Window)
        QtCore.QMetaObject.connectSlotsByName(Camera_Window)

    def retranslateUi(self, Camera_Window):
        _translate = QtCore.QCoreApplication.translate
        Camera_Window.setWindowTitle(_translate("Camera_Window", "MainWindow"))
        self.groupBox.setTitle(_translate("Camera_Window", "KONTROL"))
        self.Stop_pushButton.setText(_translate("Camera_Window", "STOP"))
        self.Start_pushButton.setText(_translate("Camera_Window", "START"))
        self.label_3.setText(_translate("Camera_Window", "KAMERA"))
        self.Off_pushButton.setText(_translate("Camera_Window", "OFF"))
        self.Camera_comboBox.setItemText(0, _translate("Camera_Window", "I. Kamera"))
        self.Camera_comboBox.setItemText(1, _translate("Camera_Window", "II. Kamera"))
        self.Camera_comboBox.setItemText(2, _translate("Camera_Window", "III. Kamera"))
        self.Camera_comboBox.setItemText(3, _translate("Camera_Window", "IV. Kamera"))
        self.Close_pushButton.setText(_translate("Camera_Window", "CLOSE"))
        self.groupBox_2.setTitle(_translate("Camera_Window", "AYRINTILAR"))
        self.label_9.setText(_translate("Camera_Window", "------"))
        self.Fps_label.setText(_translate("Camera_Window", "FPS"))
        self.label_8.setText(_translate("Camera_Window", "------"))
        self.label_10.setText(_translate("Camera_Window", "SAAT"))
        self.Calisma_label.setText(_translate("Camera_Window", "ÇALIŞMA SÜRESİ"))
        self.label_11.setText(_translate("Camera_Window", "15:03:20"))
        self.Durum_Cam.setText(_translate("Camera_Window", "KAPALI"))
        self.label_15.setText(_translate("Camera_Window", "Durum"))
        self.groupBox_3.setTitle(_translate("Camera_Window", "AYARLAR"))
        self.label_4.setText(_translate("Camera_Window", "AYAR I"))
        self.label_5.setText(_translate("Camera_Window", "AYAR II"))
        self.label_12.setText(_translate("Camera_Window", "AYAR I"))
        self.label_13.setText(_translate("Camera_Window", "AYAR II"))
        self.Ac_pushButton.setText(_translate("Camera_Window", "AÇ"))
        self.Kayit_pushButton_2.setText(_translate("Camera_Window", "KAYIT ET"))
        self.groupBox_4.setTitle(_translate("Camera_Window", "KAMERALAR"))
        self.menuAna_Sayfa.setTitle(_translate("Camera_Window", "Ana Sayfa"))
        self.menuCamera.setTitle(_translate("Camera_Window", "Camera"))

