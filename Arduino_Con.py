import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QMainWindow, QMessageBox, QTableWidgetItem             
from PyQt5 import QtCore # timer için
from ArduinoThread import *
from Hata_Goster import *

class Arduino_Toolkits():
    def __init__(self):
        self.MainWindow_Error()
    def MainWindow_Error(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_Hata_Goster_Window()
        self.ui.setupUi(self.MainWindow)
    def FeedBack_MainWindow_Error(self):
        return self.app, self.MainWindow, self.ui
    def port_ac(self,Tools):
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
        return sa.src
    def sari_led_ac(self):
        try:
            sa.ser.write(b'1')
        except:
            print("Beklenmeyen Bir Hata Sari Lamba...")
    def kirmizi_led_ac(self):
        try:
            sa.ser.write(b'3')
        except:
            print("Beklenmeyen Bir Hata Kirmizi Lamba...")
    def hepsini_kapat(self):
        try:
            sa.ser.write(b'2')
        except:
            print("Beklenmeyen Bir Hata Lambaların Kapatılması")
        self.MainWindow.close()