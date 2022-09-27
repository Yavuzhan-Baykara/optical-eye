import sqlite3
global curs
global conn
import time
import sys
import os

from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QMainWindow, QMessageBox, QTableWidgetItem, QDialog, QPushButton
from PyQt5 import QtCore # timer için
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QImage,QPixmap

from Veri_Tabani import*

from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

app3=QtWidgets.QApplication(sys.argv)
MainWindow3=QtWidgets.QMainWindow()
ui3=Ui_Veri_Tabani_Window()
ui3.setupUi(MainWindow3)
MainWindow3.show()



conn=sqlite3.connect('./Database/Tespit_Edilen_Veriler.db')
curs=conn.cursor()
sorguVeri=("""CREATE TABLE IF NOT EXISTS Hata_Sonuclari(
                 Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                 Tarih TEXT NOT NULL UNIQUE,
                 Dok No INTEGER NOT NULL,
                 Kalite_No INTEGER NOT NULL,
                 Hatanin_Geldiği_Metre INTEGER NOT NULL,
                 Bez_Eni INTEGER NOT NULL,
                 Hatanin_Duvar_Tarafından_Mesafesi INTEGER NOT NULL,
                 Hata_Eni INTEGER NOT NULL,
                 Hata_Boyutu INTEGER NOT NULL,
                 Hata_Alanı INTEGER NOT NULL,
                 Hata_Sınıfı TEXT NOT NULL,
                 Hata_No INTEGER NOT NULL,
                 Kamera_No TEXT NOT NULL)
                 """)

curs.execute(sorguVeri)
conn.commit()

def Listele():
    ui3.Veri_Tabani_Widget.clear()
    ui3.Veri_Tabani_Widget.setHorizontalHeaderLabels(('Id','Tarih','Dok No','Kalite_No','Hatanin_Geldiği_Metre','Bez_Eni','Hatanin_Duvar_Tarafından_Mesafesi','Hata_Eni','Hata_Boyutu','Hata_Alanı','Hata_Sınıfı','Hata_No','Kamera_No'))
    curs.execute("SELECT * FROM Hata_Sonuclari")
    for satirIndeks, satirVeri in enumerate(curs):
        for sutunIndeks, sutunVeri in enumerate (satirVeri):
            ui3.Veri_Tabani_Widget.setItem(satirIndeks,sutunIndeks,QTableWidgetItem(str(sutunVeri)))
            
def Doldur():
    selected=ui3.Veri_Tabani_Widget.selectedItems()
    #Id Yok
    #Tarih Yok
    ui3.Dok_No_LineEdit.setText(selected[2].text())
    #Kalite No Yok
    ui3.Metre_LineEdit.setText(selected[4].text())
    ui3.Duvar_Mesafe_LineEdit.setText(selected[6].text())
    ui3.Hata_Eni_LineEdit.setText(selected[7].text())
    ui3.Hata_Boyutu_LineEdit.setText(selected[8].text())
    ui3.Hata_Alani_LineEdit.setText(selected[9].text())
    ui3.Sinifi_LineEdit.setText(selected[10].text())

    
def Ara():
    aranan1=""
    if ui3.Leke_radioButton.isChecked():
        aranan1=ui3.Leke_radioButton.text()
    if ui3.Iplik_RadioButton.isChecked():
        aranan1=ui3.Iplik_RadioButton.text()
    if ui3.Yatay_RadioButton.isChecked():
        aranan1=ui3.Yatay_RadioButton.text()
    if ui3.Delik_RadioButton.isChecked():
        aranan1=ui3.Delik_RadioButton.text()  
    if ui3.Yag_RadioButton.isChecked():
        aranan1=ui3.Yag_RadioButton.text()  
    if ui3.Dikey_RadioButton.isChecked():
        aranan1=ui3.Dikey_RadioButton.text()
    

    curs.execute("SELECT * FROM Hata_Sonuclari WHERE Hata_Sınıfı=?",(aranan1,))
    conn.commit()
    ui3.Veri_Tabani_Widget.clear()
    ui3.Veri_Tabani_Widget.setHorizontalHeaderLabels(('Id','Tarih','Dok No','Kalite_No','Hatanin_Geldiği_Metre','Bez_Eni','Hatanin_Duvar_Tarafından_Mesafesi','Hata_Eni','Hata_Boyutu','Hata_Alanı','Hata_Sınıfı','Hata_No','Kamera_No'))
    
    for satirIndeks, satirVeri in enumerate(curs):
        for sutunIndeks, sutunVeri in enumerate (satirVeri):
            ui3.Veri_Tabani_Widget.setItem(satirIndeks,sutunIndeks,QTableWidgetItem(str(sutunVeri)))
            
    if ui3.Tumu_RadioButton.isChecked():
        Listele()
    Button_Show()

def Clear():
    

    ui3.Veri_Tabani_Widget.clear()
    ui3.Veri_Tabani_Widget.setHorizontalHeaderLabels(('Id','Tarih','Dok No','Kalite_No','Hatanin_Geldiği_Metre','Bez_Eni','Hatanin_Duvar_Tarafından_Mesafesi','Hata_Eni','Hata_Boyutu','Hata_Alanı','Hata_Sınıfı','Hata_No','Kamera_No'))
    Button_Show()
def Button_Show():
    table=ui3.Veri_Tabani_Widget

    last_row = table.rowCount()
    table.setRowCount(table.rowCount())
    for i in range(table.rowCount()):
        row = last_row+i
        button = QtWidgets.QPushButton('Goster', MainWindow3)
        button.clicked.connect(lambda _, x=i: print('button', x))
        table.setCellWidget(row, 0, button)
        table.setCellWidget(i, 0, button)  
        if i==table.rowCount():
            break

      
Listele()  
Button_Show()

        
ui3.Temiz_pushButton.clicked.connect(Clear)
ui3.Veri_Tabani_Widget.itemSelectionChanged.connect(Doldur)
ui3.Goster_pushButton.clicked.connect(Ara)
sys.exit(app3.exec_())