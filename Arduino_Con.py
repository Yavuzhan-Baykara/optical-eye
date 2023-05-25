import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QMainWindow, QMessageBox, QTableWidgetItem             
from PyQt5 import QtCore # timer için
from ArduinoThread import *
from Hata_Goster import *

class Arduino_Toolkits():
    def __init__(self):
        self.MainWindow_Error()
        self.warning_status:bool = False 
    def MainWindow_Error(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_Hata_Goster_Window()
        self.ui.setupUi(self.MainWindow)
    def FeedBack_MainWindow_Error(self):
        return self.app, self.MainWindow, self.ui
    def port_ac(self,Tools):
        try:
            port,baud=Tools.feedback_Import_Serial_Port()
            self.port=str(port)
            self.baud=str(baud)
            global sa
            sa=AThread(self.port,self.baud).start()
            if sa.ser.is_open:
                print("Port açıldı...")
                global timer1
                timer1 = QtCore.QTimer()
                timer1.start(100)
                # timer1.timeout.connect(self.sensoroku)
            else:
                print(" Port açılamadı !!!")
        except serial.SerialException as e:
            print("Serial açılırken hata tespit edildi...", e)
    def port_kapat(self):
        try:
            if sa.ser.is_open:
                sa.ser.close()
                timer1.stop()
                print("Port kapatıldı...")
                sa.stop()
        except:
            print("Beklenmeyen Bir Hata Port Kapatırken Bir Sorun Oluştu...")
    def Feedback_src(self):
        try:
            if sa.inp:
                if len(sa.inp) > 2:
                    return sa.inp[0:2]
                elif len(sa.inp) == 2:
                    return sa.src
                else:
                    return [0,0]
            else:
                return [0,0]
        except Exception as e:
            [0,0]
            # print(f"Bir sorun oluştu: {e}")    
    def sari_led_ac(self):
        try:
            sa.ser.write(b'A')
        except:
            print("Beklenmeyen Bir Hata Sari Lamba...")
    def kirmizi_led_ac(self):
        try:
            sa.ser.write(b'C')
            self.warning_status = True 
        except:
            print("Beklenmeyen Bir Hata Kirmizi Lamba...")
    def hepsini_kapat(self):
        try:
            self.warning_status = False
            sa.ser.write(b'B')
            sa.ser.write(b'D')
        except:
            print("Beklenmeyen Bir Hata Lambaların Kapatılması")
        self.MainWindow.close()
    def setBrightness(self, value:str = 0):
        try:
            sa.ser.write(str(value).encode())
            sleep(1)
            print("Başarılı")
        except:
            print("Beklenmeyen Bir Işık Ayarı...")