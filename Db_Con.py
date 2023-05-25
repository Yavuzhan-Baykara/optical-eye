import sqlite3
from turtle import width
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
# MainWindow3.setWindowFlag(Qt.FramelessWindowHint)
####################################


from Goster import*
############Veri Tabani#############
app4=QtWidgets.QApplication(sys.argv)
MainWindow4=QtWidgets.QMainWindow()
ui4=Ui_Goster_Window()
# MainWindow4.setWindowFlag(Qt.FramelessWindowHint)
ui4.setupUi(MainWindow4)
####################################
onlyInt = QIntValidator()
ui3.Gunclle_PushButton.setDisabled(True)
ui3.Delete_PushButton.setDisabled(True)


conn=sqlite3.connect('./Database/Tespit_Edilen_Veriler.db',timeout=1, check_same_thread=False)
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
                 Sonuc_Isım INTEGER NOT NULL)
                 """)

curs.execute(sorguVeri)
conn.commit()
class Veri_Tabani_Window():
    def __init__(self, ):
        self.details = None

    def Button_Show(self, i, row):
        table=ui3.Veri_Tabani_Widget
        button = QtWidgets.QPushButton('Goster', MainWindow3)
        button.clicked.connect(lambda _, x=i: self.Goster(x))
        table.setCellWidget(row, 0, button)
    def Listele(self):
        def Button_Show(i, row):
            table=ui3.Veri_Tabani_Widget
            button = QtWidgets.QPushButton('Goster', MainWindow3)
            button.clicked.connect(lambda _, x=i: self.Goster(x))
            table.setCellWidget(row, 0, button)
        ui3.Veri_Tabani_Widget.setSelectionBehavior(QAbstractItemView.SelectRows)
        ui3.Veri_Tabani_Widget.clear()
        ui3.Veri_Tabani_Widget.setHorizontalHeaderLabels(('Id','Tarih','Dok_No','Kalite_No','Hatanin_Geldiği_Metre','Bez_Eni','Hatanin_Duvar_Tarafından_Mesafesi','Hata_Eni','Hata_Boyutu','Hata_Alanı','Hata_Sınıfı','Sonuc_Isım'))
        result = curs.execute("SELECT * FROM Hata_Sonuclari ORDER BY id DESC LIMIT 10000")
        cnt = 0
        for satirIndeks, satirVeri in enumerate(result):
            for sutunIndeks, sutunVeri in enumerate (satirVeri):
                ui3.Veri_Tabani_Widget.setItem(satirIndeks,sutunIndeks,QTableWidgetItem(str(sutunVeri)))
            Button_Show(satirVeri[0], cnt)
            cnt+=1
            if cnt == 10000:
                return
    def Doldur(self):
        selected=ui3.Veri_Tabani_Widget.selectedItems()
        if selected:
            try:
                ui3.Metre_LineEdit.setText(selected[4].text())
                ui3.Hata_Alani_LineEdit.setText(selected[9].text())
                ui3.Sinifi_LineEdit.setText(selected[10].text())
                ui3.Gunclle_PushButton.setDisabled(False)
                ui3.Delete_PushButton.setDisabled(False)
            except:
                pass
    def Goster(self, Id):
        curs.execute("SELECT * FROM Hata_Sonuclari WHERE Id='%s'" %(Id))
        conn.commit()
        Data = curs.fetchall()
        for row in Data:
            if not Data==None:
                try: 
                    MainWindow4.close()
                    MainWindow4.show()
                    ui4.Duvar_Label.setText(str(row[6]))
                    ui4.Eni_Label.setText(str(row[7]))
                    ui4.boyu_Label.setText(str(row[8]))
                    ui4.Alan_Label.setText(str(row[9]))
                    ui4.Metre_Label.setText(str(row[4]))
                    ui4.Sinif_Label.setText(str(row[10]))
                    x1, x2, y1, y2 = [int(coord) for coord in row[12].split(", ")]
                    img_Goster = cv2.imread(row[11])
                    img_Goster = img_Goster[y1-5:y2+5,x1-5:x2+5]
                    img_Goster=cv2.resize(img_Goster, (320,320),interpolation=cv2.INTER_CUBIC)
                    image = QtGui.QImage(img_Goster.data, img_Goster.shape[1], img_Goster.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
                    ### Doldurma Göster Window
                    ui4.Goster_Label.setPixmap(QtGui.QPixmap.fromImage(image))
                    return str(row[11])
                except Exception as e:
                    print(e.__class__)

        
    def Id_Bul(self, name):
        curs.execute("SELECT * FROM Hata_Sonuclari WHERE Sonuc_Isım='%s'" %(name))
        conn.commit()
        Data = curs.fetchall()
        for row in Data:
            print(row[0])
             
    def Ara(self):
        aranan1=""
        if ui3.Leke_radioButton.isChecked():
            aranan1=ui3.Leke_radioButton.text()
        if ui3.Iplik_RadioButton.isChecked():
            aranan1=ui3.Iplik_RadioButton.text()
        if ui3.Yatay_RadioButton.isChecked():
            aranan1=ui3.Yatay_RadioButton.text()
        if ui3.Delik_RadioButton.isChecked():
            aranan1=ui3.Delik_RadioButton.text()  
        if ui3.Dikey_RadioButton.isChecked():
            aranan1=ui3.Dikey_RadioButton.text()

        curs.execute("SELECT * FROM Hata_Sonuclari WHERE Hata_Sınıfı=? ORDER BY id DESC LIMIT 10000",(aranan1,))
        conn.commit()
        ui3.Veri_Tabani_Widget.clear()
        ui3.Veri_Tabani_Widget.setHorizontalHeaderLabels(('Id','Tarih','Dok_No','Kalite_No','Hatanin_Geldiği_Metre','Bez_Eni','Hatanin_Duvar_Tarafından_Mesafesi','Hata_Eni','Hata_Boyutu','Hata_Alanı','Hata_Sınıfı','Sonuc_Isım'))
        cnt = 0
        for satirIndeks, satirVeri in enumerate(curs):
            for sutunIndeks, sutunVeri in enumerate (satirVeri):
                ui3.Veri_Tabani_Widget.setItem(satirIndeks,sutunIndeks,QTableWidgetItem(str(sutunVeri)))
            self.Button_Show(satirVeri[0], cnt)
            cnt+=1    
        if ui3.Tumu_RadioButton.isChecked():
            self.Listele()
       
    def get_last_Heigt_Width(self):
        curs.execute("SELECT Camera_Height, Camera_Width, Camera_İmpact_Rate FROM  Cameras_Inf ORDER BY Id DESC LIMIT 1")
        conn.commit()
        path = curs.fetchone()
        _Height,_Width,_Camera_İmpact_Rate=path
        return _Height,_Width,_Camera_İmpact_Rate

    def get_last_path(self):
        curs.execute("SELECT path FROM  Son_Kullanilan ORDER BY Id DESC LIMIT 1")
        conn.commit()
        path = curs.fetchone()[0]
        path = os.path.normpath(path)
        return path

    def get_last_model_path(self):
        curs.execute("SELECT path FROM  Son_Kullanilan_Model ORDER BY Id DESC LIMIT 1")
        conn.commit()
        path = curs.fetchone()[0]
        path = os.path.normpath(path)
        return path
    
    def set_last_model_path(self, path):
        curs.execute("""INSERT INTO Son_Kullanilan_Model 
                        (path)
                        VALUES
                        (?)
        """,(path,))
        conn.commit()
    
    def set_last_path(self, path):
        curs.execute("""INSERT INTO Son_Kullanilan 
                        (path)
                        VALUES
                        (?)
        """,(path,))
        conn.commit()
    
    def get_last_data(self):
        curs.execute("SELECT Camera_Height, Camera_Width, Camera_İmpact_Rate, Camera_Serial, Camera_Exposure_Time, Camera_Cut_Off, Camera_Type FROM Cameras_Inf ORDER BY Id DESC LIMIT 1")
        conn.commit()
        path = curs.fetchall()
        return path

    def Last_Cameras_Info_Add(self, Camera_Height, Camera_Width, Camera_Impact_Rate, Camera_Serial, Camera_Exposure_Time, Camera_Cut_Off, Camera_Type):
        print(str(Camera_Serial[0]))
        Camera_Serials = Camera_Serial[0]+','+Camera_Serial[1]+','+Camera_Serial[2]+','+Camera_Serial[3]
        Cameras_Type = Camera_Type[0]+','+Camera_Type[1]+','+Camera_Type[2]+','+Camera_Type[3]
        Camera_Exposure_Times = Camera_Exposure_Time[0]+','+Camera_Exposure_Time[1]+','+Camera_Exposure_Time[2]+','+Camera_Exposure_Time[3]
        curs.execute("""
        INSERT INTO Cameras_Inf
        (Camera_Height, Camera_Width, Camera_İmpact_Rate, Camera_Serial, Camera_Exposure_Time, Camera_Cut_Off, Camera_Type)
        VALUES
        (?,?,?,?,?,?,?)""",
        ( Camera_Height, Camera_Width, Camera_Impact_Rate, Camera_Serials, Camera_Exposure_Times, Camera_Cut_Off, Cameras_Type))
        conn.commit()

    def get_users_inf(self):
        curs.execute("SELECT * FROM Kullanicilar")
        conn.commit()
        users = curs.fetchall()
        return users

    def set_users_inf(self, Kullanici_adi, Sifre):
        try:
            curs.execute("INSERT INTO Kullanicilar (Kullanici_adi, Sifre) VALUES (?,?)", (Kullanici_adi, Sifre))
            conn.commit()
        except sqlite3.Error as er:
            ui3.statusbar.showMessage(" " * 1 + f"Bir sorun oluştu: {er} ",1500)
            print(er)

    def Clear(self):
        ui3.Veri_Tabani_Widget.clear()
        ui3.Veri_Tabani_Widget.setHorizontalHeaderLabels(('Id','Tarih','Dok_No','Kalite_No','Hatanin_Geldiği_Metre','Bez_Eni','Hatanin_Duvar_Tarafından_Mesafesi','Hata_Eni','Hata_Boyutu','Hata_Alanı','Hata_Sınıfı','Sonuc_Isım'))
        MainWindow3.show()
    
    def Ekle(self, Tarih,Dok_No,Kalite_No,Hatanın_Geldiği_Metre,Bez_Eni,Hatanin_Duvar_Tarafından_Mesafesi,Hata_Eni,Hata_Boyutu,Hata_Alanı,Hata_Sınıfı,Sonuc_Isım, Hata_Koordinant):
        with sqlite3.connect("./Database/Tespit_Edilen_Veriler.db") as conn:
            curs = conn.cursor()
            curs.execute("""INSERT INTO Hata_Sonuclari
                        (Tarih,Dok_No,Kalite_No,Hatanin_Geldiği_Metre,Bez_Eni,Hatanin_Duvar_Tarafından_Mesafesi,Hata_Eni,Hata_Boyutu,Hata_Alanı,Hata_Sınıfı,Sonuc_Isım, Hata_Koordinant)
                        VALUES
                        (?,?,?,?,?,?,?,?,?,?,?,?)""",
                        (Tarih, Dok_No, Kalite_No, Hatanın_Geldiği_Metre, Bez_Eni, Hatanin_Duvar_Tarafından_Mesafesi, Hata_Eni, Hata_Boyutu, Hata_Alanı, Hata_Sınıfı, Sonuc_Isım, Hata_Koordinant))
            conn.commit()
        
    
    def Update(self):
        selected = ui3.Veri_Tabani_Widget.selectedItems()
        if selected:
            Id = int(selected[0].text())
            alan = int(float(ui3.Hata_Alani_LineEdit.text()))
            meter = int(float(ui3.Metre_LineEdit.text()))
            sinif = str(ui3.Sinifi_LineEdit.text())
        try:
            curs.execute(""" Update Hata_Sonuclari SET Hata_Alanı=?, Hatanin_Geldiği_Metre=?, Hata_Sınıfı=?  WHERE Id=?""", (str(alan),str(meter), str(sinif), str(Id),))
            conn.commit()
        except sqlite3.Error as error:
            ui3.Gunclle_PushButton.setDisabled(True)
            ui3.Delete_PushButton.setDisabled(True)
            ui3.statusbar.showMessage(" " * 1 + f"Veri tabanında bir sorun oluştu. {error}", 1500)
            print("Failed to update sqlite table: ", error)
        finally:
            ui3.Gunclle_PushButton.setDisabled(True)
            ui3.Delete_PushButton.setDisabled(True)
            self.Listele()

    def Delete(self):
        selected = ui3.Veri_Tabani_Widget.selectedItems()
        if selected:
            Id = int(selected[0].text())
        try: 
            sql_delete_query = """DELETE from Hata_Sonuclari where id = ?"""
            curs.execute(sql_delete_query, (Id,))
            conn.commit()
        except sqlite3.Error as error:
            ui3.Gunclle_PushButton.setDisabled(True)
            ui3.Delete_PushButton.setDisabled(True)
            ui3.statusbar.showMessage(" " * 1 + f"Veri tabanında bir sorun oluştu. {error}", 1500)
            print("Failed to update sqlite table: ",error)
        finally:
            ui3.Delete_PushButton.setDisabled(True)
            ui3.Gunclle_PushButton.setDisabled(True)
            self.Listele()

    def set_fabric_settings(self, kumas_ismi, isik_siddeti):
        try:
            curs.execute("INSERT INTO Kumas_ayari (kumas_ismi, ısık_siddeti) VALUES (?,?)", (kumas_ismi, isik_siddeti))
            conn.commit()
            print("Veri başarıyla eklendi.")
            
        except sqlite3.IntegrityError:
            print("Bu kumaş ismi zaten kayıtlı.")
            try:
                curs.execute("UPDATE Kumas_ayari SET ısık_siddeti = ? WHERE kumas_ismi = ?", (isik_siddeti, kumas_ismi))
                conn.commit()
                print("Veri başarıyla güncellendi.")
            except:
                print("Veri güncellenirken hata oluştu.")
    
    def get_fabric_name(self):
        curs.execute("SELECT kumas_ismi FROM Kumas_ayari")
        fabric_names = [row[0] for row in curs.fetchall()]
        return fabric_names
    def get_fabric_brightness(self, kumas_ismi):
        try:
            curs.execute("SELECT ısık_siddeti FROM Kumas_ayari WHERE kumas_ismi=?", (kumas_ismi,))
            result = curs.fetchone()
            if result:
                return result[0]
            else:
                print("Bu isimde bir kumaş verisi bulunamadı.")
        except sqlite3.Error as error:
            print("Veri çekilirken hata oluştu:", error)
    
    def set_Camera_Local_Settings(self, local_height, vision_weight, vision_height, vision_angle):
        try:
            curs.execute("INSERT INTO Camera_local_inf (Camera_local_height, Camera_vision_weight, Camera_vision_height, Camera_vision_angle) VALUES (?,?,?,?)", (local_height, vision_weight, vision_height, vision_angle))
            conn.commit()
            print("Veri başarıyla eklendi")
        except:
            print("Veri güncellenirken hata oluştu.")
    def get_Camera_Local_Settings(self):
        try:
            curs.execute("SELECT * FROM Camera_local_inf ORDER BY Camera_local_height DESC LIMIT 1")
            result = curs.fetchone()
            print(result)
            local_height = result[0]
            vision_weight = result[1]
            vision_height = result[2]
            vision_angle = result[3]
            return local_height, vision_weight, vision_height, vision_angle
        except:
            print("Veriler alınırken hata oluştu.")
            return 200, 200, 200, 200
    def details_show(self, tarih, dok_no, kalite_no):
        aranan1 = ""
        radio_buttons = [
            ui3.Leke_radioButton,
            ui3.Iplik_RadioButton,
            ui3.Yatay_RadioButton,
            ui3.Delik_RadioButton,
            ui3.Dikey_RadioButton
        ]

        for button in radio_buttons:
            if button.isChecked():
                aranan1 = button.text()
                sql = "SELECT * FROM Hata_Sonuclari WHERE Tarih=? AND Dok_No=? AND Kalite_No=? AND Hata_Sınıfı=?"
                result = curs.execute(sql, (tarih, dok_no, kalite_no, aranan1))
                break
        else:
            sql = "SELECT * FROM Hata_Sonuclari WHERE Tarih=? AND Dok_No=? AND Kalite_No=?"
            result = curs.execute(sql, (tarih, dok_no, kalite_no))

        def Button_Show(i, row):
            table=ui3.Veri_Tabani_Widget
            button = QtWidgets.QPushButton('Goster', MainWindow3)
            button.clicked.connect(lambda _, x=i: self.Goster(x))
            table.setCellWidget(row, 0, button)
        
        ui3.Veri_Tabani_Widget.clear()
        ui3.Veri_Tabani_Widget.setHorizontalHeaderLabels(('Id','Tarih','Dok_No','Kalite_No','Hatanin_Geldiği_Metre','Bez_Eni','Hatanin_Duvar_Tarafından_Mesafesi','Hata_Eni','Hata_Boyutu','Hata_Alanı','Hata_Sınıfı','Sonuc_Isım'))
        cnt = 0
        for satirIndeks, satirVeri in enumerate(result):
            for sutunIndeks, sutunVeri in enumerate(satirVeri):
                ui3.Veri_Tabani_Widget.setItem(satirIndeks, sutunIndeks, QTableWidgetItem(str(sutunVeri)))
            Button_Show(satirVeri[0], cnt)
            cnt += 1
            if cnt == 1000:
                return
        ui3.Veri_Tabani_Widget.verticalScrollBar().setValue(0)
        return [tarih, dok_no, kalite_no]
    def filter(self):
        def show_details(x,y,z):
            self.details = self.details_show(x,y,z)
        def Button_Show(i, j, k, row):
            table=ui3.Veri_Tabani_Widget
            button = QtWidgets.QPushButton('Goster')
            button.clicked.connect(lambda _, x=i, y=j, z=k: show_details(x, y, z))
            table.setCellWidget(row, 0, button)
        widget_1 = ui3.calendarWidget.selectedDate()
        widget_2 = ui3.calendarWidget_2.selectedDate()
        Date = [str(widget_1.day()), str(widget_1.month()), str(widget_1.year())]
        DateLast = [str(widget_2.day()), str(widget_2.month()), str(widget_2.year())]
        Split_Date=str(int(Date[0]))+'.'+str(int(Date[1]))+'.'+str(int(Date[2]))
        Split_Date_last=str(int(DateLast[0]))+'.'+str(int(DateLast[1]))+'.'+str(int(DateLast[2]))
        print("başlangıç" + str(Split_Date))
        print("sonuç" + str(Split_Date_last))
        sql = "SELECT DISTINCT Tarih, Dok_No, Kalite_No FROM Hata_Sonuclari WHERE Tarih BETWEEN ? AND ?"
        result = curs.execute(sql, (Split_Date, Split_Date_last))
        ui3.Veri_Tabani_Widget.clear()
        ui3.Veri_Tabani_Widget.setHorizontalHeaderLabels(('Id','Tarih','Dok_No','Kalite_No'))
        cnt = 0
        id = 1
        for satirIndeks, satirVeri in enumerate(result):
            # id değerini demetin başına ekle
            row = (id,) + satirVeri
            # Verileri ekrana yazdır
            for sutunIndeks, sutunVeri in enumerate(row):
                ui3.Veri_Tabani_Widget.setItem(satirIndeks, sutunIndeks, QTableWidgetItem(str(sutunVeri)))
            # Buton göster
            Button_Show(satirVeri[0], satirVeri[1], satirVeri[2], id-1)
            # id değerini arttır
            id += 1
        ui3.Veri_Tabani_Widget.verticalScrollBar().setValue(0)
        
    def mail_key_show(self):
        sql = "SELECT email, key FROM Mail"
        curs.execute(sql)
        email_data = curs.fetchall()[0]
        return email_data
    
    def mail_show(self):
        sql = "SELECT email  FROM Mail"
        curs.execute(sql)
        email_data = curs.fetchall()
        return email_data
    
    def mail_delete(self, select_item):
        sql = "DELETE FROM Mail WHERE email=?"
        if select_item is not None:
            print(select_item)
            try:
                curs.execute(sql, (select_item,))
                conn.commit()
            except:
                pass
    def mail_add(self, item):
        if item is not None:
            curs.execute("INSERT INTO Mail (email) VALUES (?)", (item,))
            conn.commit()
    def get_details(self):
        return self.details