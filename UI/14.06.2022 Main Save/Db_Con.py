import sqlite3
global curs
global conn
import time
import sys
import os
import cv2

from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QMainWindow, QMessageBox, QTableWidgetItem, QDialog, QPushButton
from PyQt5 import QtCore # timer için
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QImage,QPixmap

from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *



from Veri_Tabani import*
############Veri Tabani#############
app3=QtWidgets.QApplication(sys.argv)
MainWindow3=QtWidgets.QMainWindow()
ui3=Ui_Veri_Tabani_Window()
ui3.setupUi(MainWindow3)
####################################


from Goster import*
############Veri Tabani#############
app4=QtWidgets.QApplication(sys.argv)
MainWindow4=QtWidgets.QMainWindow()
ui4=Ui_Goster_Window()
ui4.setupUi(MainWindow4)
####################################


conn=sqlite3.connect('./Database/Tespit_Edilen_Veriler.db',timeout=1)
curs=conn.cursor()
sorguVeri=("""CREATE TABLE IF NOT EXISTS Hata_Sonuclari(
                 Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                 Tarih TEXT NOT NULL UNIQUE,
                 Dok_No INTEGER NOT NULL,
                 Kalite_No INTEGER NOT NULL,
                 Hatanin_Geldiği_Metre INTEGER NOT NULL,
                 Bez_Eni INTEGER NOT NULL,
                 Hatanin_Duvar_Tarafından_Mesafesi INTEGER NOT NULL,
                 Hata_Eni INTEGER NOT NULL,
                 Hata_Boyutu INTEGER NOT NULL,
                 Hata_Alanı INTEGER NOT NULL,
                 Hata_Sınıfı TEXT NOT NULL,
                 Sonuc_Isım INTEGER NOT NULL,
                 Kamera_No TEXT NOT NULL)
                 """)


curs.execute(sorguVeri)
conn.commit()
class Veri_Tabani_Window():
    def Listele():
        ui3.Veri_Tabani_Widget.clear()
        ui3.Veri_Tabani_Widget.setHorizontalHeaderLabels(('Id','Tarih','Dok_No','Kalite_No','Hatanin_Geldiği_Metre','Bez_Eni','Hatanin_Duvar_Tarafından_Mesafesi','Hata_Eni','Hata_Boyutu','Hata_Alanı','Hata_Sınıfı','Sonuc_Isım','Kamera_No'))
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
    
    
    def Goster(Id):
        curs.execute("SELECT * FROM Hata_Sonuclari WHERE Id='%s'" %(Id))
        conn.commit()
        Data = curs.fetchall()
        for row in Data:
            if not Data==None:
                MainWindow4.close()
                MainWindow4.show()
                img_Goster=cv2.imread(row[11])
                img_Goster=cv2.resize(img_Goster, (320,320),interpolation=cv2.INTER_CUBIC)
                image = QtGui.QImage(img_Goster.data, img_Goster.shape[1], img_Goster.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
                
                ### Doldurma Göster Window
                ui4.Goster_Label.setPixmap(QtGui.QPixmap.fromImage(image))
               
                ui4.Duvar_Label.setText(str(row[6]))
                ui4.Eni_Label.setText(str(row[7]))
                ui4.boyu_Label.setText(str(row[8]))
                ui4.Alan_Label.setText(str(row[9]))
                ui4.Metre_Label.setText(str(row[4]))
                ui4.Sinif_Label.setText(str(row[10]))
                ui4.Isim_Label.setText(str(row[11]))
            
        
        
            
        
        
        
    def Button_Show():
        table=ui3.Veri_Tabani_Widget
        last_row = table.rowCount()
        table.setRowCount(table.rowCount())
        for i in range(table.rowCount()):
            row = last_row+i
            button = QtWidgets.QPushButton('Goster', MainWindow3)
            button.clicked.connect(lambda _, x=i: Veri_Tabani_Window.Goster(x))
            
            table.setCellWidget(row, 0, button)
            table.setCellWidget(i, 0, button)
            
            # if i==table.rowCount():
            #     break    
    
        
        
        
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
        if ui3.Kirik_RadioButton.isChecked():
            aranan1="Kirisik"
        
    
        curs.execute("SELECT * FROM Hata_Sonuclari WHERE Hata_Sınıfı=?",(aranan1,))
        conn.commit()
        ui3.Veri_Tabani_Widget.clear()
        ui3.Veri_Tabani_Widget.setHorizontalHeaderLabels(('Id','Tarih','Dok_No','Kalite_No','Hatanin_Geldiği_Metre','Bez_Eni','Hatanin_Duvar_Tarafından_Mesafesi','Hata_Eni','Hata_Boyutu','Hata_Alanı','Hata_Sınıfı','Sonuc_Isım','Kamera_No'))
        
        for satirIndeks, satirVeri in enumerate(curs):
            for sutunIndeks, sutunVeri in enumerate (satirVeri):
                ui3.Veri_Tabani_Widget.setItem(satirIndeks,sutunIndeks,QTableWidgetItem(str(sutunVeri)))
                
        if ui3.Tumu_RadioButton.isChecked():
            Veri_Tabani_Window.Listele()
        Veri_Tabani_Window.Button_Show()
    
    def Clear():
        ui3.Veri_Tabani_Widget.clear()
        ui3.Veri_Tabani_Widget.setHorizontalHeaderLabels(('Id','Tarih','Dok_No','Kalite_No','Hatanin_Geldiği_Metre','Bez_Eni','Hatanin_Duvar_Tarafından_Mesafesi','Hata_Eni','Hata_Boyutu','Hata_Alanı','Hata_Sınıfı','Sonuc_Isım','Kamera_No'))
        Veri_Tabani_Window.Button_Show()
        MainWindow3.show()
    
    def Ekle(Tarih,Dok_No,Kalite_No,Hatanın_Geldiği_Metre,Bez_Eni,Hatanin_Duvar_Tarafından_Mesafesi,Hata_Eni,Hata_Boyutu,Hata_Alanı,Hata_Sınıfı,Sonuc_Isım,Kamera_No):
        curs.execute("""INSERT INTO Hata_Sonuclari
                     (Tarih,Dok_No,Kalite_No,Hatanın_Geldiği_Metre,Bez_Eni,Hatanin_Duvar_Tarafından_Mesafesi,Hata_Eni,Hata_Boyutu,Hata_Alanı,Hata_Sınıfı,Sonuc_Isım,Kamera_No)
                     VALUES
                     (?,?,?,?,?,?,?,?,?,?,?,?)""",
                     (Tarih,Dok_No,Kalite_No,Hatanın_Geldiği_Metre,Bez_Eni,Hatanin_Duvar_Tarafından_Mesafesi,Hata_Eni,Hata_Boyutu,Hata_Alanı,Hata_Sınıfı,Sonuc_Isım,Kamera_No))
            
        conn.commit()
        Veri_Tabani_Window.Listele()
    

    # Listele()  
    # Button_Show()
    
