from array import array
from typing import Any
from PyQt5 import *
import re

class GirisVKayit():
    def __init__(self, app1, ui1, ui2, ui8, MainWindow1, MainWindow2, MainWindow8, users, db):
        self.app1=app1
        self.ui1=ui1
        self.ui2=ui2
        self.ui8=ui8
        self.MainWindow1 = MainWindow1
        self.MainWindow2 = MainWindow2
        self.MainWindow8 = MainWindow8
        self.db=db
        global name
        global password
        self.users=users
        print(self.users)

    def Inf(self) -> list:
        name=self.ui1.Kullaniciadi_lineEdit.text()
        password=self.ui1.Sifre_lineEdit.text()
        Login=[name, password]
        return Login
        
    def Giris(self, choice) -> Any:
        'choise: Camera // Camera Window choise: Kayit // Kayit_Ol Window'
        ...
        login=self.Inf() 
        for i in range(len(self.users)):
            if(self.users[i][0] == login[0] and self.users[i][1] == login[1] and choice == "Camera"):
                self.MainWindow1.close()
                self.MainWindow2.showMaximized()
            elif(self.users[i][0] == login[0] and self.users[i][1] == login[1] and choice == "Kayit"):
                self.MainWindow8.show()
            else:
                print("başarısız")
    
    def kayit(self):
        kullanici_adi = self.ui8.Kullanici_adi_lineEdit.text()
        sifre = self.ui8.Sifre_lineEdit.text()
        sifre_tekrar = self.ui8.Sifre_tekrar_lineEdit.text()
        telefon = self.ui8.Telefon_lineEdit.text()
        eposta = self.ui8.E_posta_lineEdit.text()
        self.db.set_users_inf(kullanici_adi, sifre)
