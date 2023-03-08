from os import mkdir
import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi
from cv2 import CAP_AVFOUNDATION
from torch import true_divide
from Camera import*
from Giris import*
from Db_Con import *
import Db_Con as DC
from admin_page import * 
from Port import*
from Kayit_Ol import*
import json
from FaultyFabricWindow import *
from Warning_window import *
from PyQt5.QtGui import QPixmap

class ToolKit():
    def Windows(self):
        self.Model_Path=Veri_Tabani_Window.get_last_model_path()
        ############ Giris ############################
        self.app1=QtWidgets.QApplication(sys.argv)    #
        self.MainWindow1=QtWidgets.QMainWindow()      #
        self.ui1= Ui_Giris_Window()                   #
        #self.MainWindow1.setWindowFlag(Qt.FramelessWindowHint)
        self.ui1.setupUi(self.MainWindow1)            #
        ###############################################

        ############ Camera ###########################
        self.app2=QtWidgets.QApplication(sys.argv)    #
        self.MainWindow2=QtWidgets.QMainWindow()      #
        self.app2.setWindowIcon(QtGui.QIcon('./Icon/MainWindow/mmm.png'))
        #self.MainWindow2.setWindowFlag(Qt.FramelessWindowHint)
        self.ui2=Ui_Camera_Window()                   #
        self.ui2.setupUi(self.MainWindow2)            #
        ###############################################

        ############ Veri Tabani ######################
        self.app3=QtWidgets.QApplication(sys.argv)    #
        self.MainWindow3=QtWidgets.QMainWindow()      #
        self.ui3=Ui_Veri_Tabani_Window()              #
        #self.MainWindow3.setWindowFlag(Qt.FramelessWindowHint)
        self.ui3.setupUi(self.MainWindow3)            #
        ###############################################

        ############ Göster ################40113349###
        self.app4=QtWidgets.QApplication(sys.argv)    #
        self.MainWindow4=QtWidgets.QMainWindow()      #
        self.ui4=Ui_Goster_Window()                   #
        #self.MainWindow4.setWindowFlag(Qt.FramelessWindowHint)
        self.ui4.setupUi(self.MainWindow4)            #
        ###############################################

        ############ Admin_P ##########################
        self.app5=QtWidgets.QApplication(sys.argv)    #
        self.MainWindow5=QtWidgets.QMainWindow()      #
        self.ui5=Ui_MainWindow()                      #
        #self.MainWindow5.setWindowFlag(Qt.FramelessWindowHint)
        self.ui5.setupUi(self.MainWindow5)            #
        ###############################################

        ############ Port Sorgula #####################
        self.app6=QtWidgets.QApplication(sys.argv)    #
        self.MainWindow6=QtWidgets.QMainWindow()      #
        self.ui6=Ui_Port_Window()                     #
        #self.MainWindow6.setWindowFlag(Qt.FramelessWindowHint)
        self.ui6.setupUi(self.MainWindow6)            #
        ###############################################

        ################ Kayıt Ol #####################
        self.app7=QtWidgets.QApplication(sys.argv)    #
        self.MainWindow7=QtWidgets.QMainWindow()      #
        self.ui7=Ui_Kayt_Ol()                         #
        #self.MainWindow7.setWindowFlag(Qt.FramelessWindowHint)
        self.ui7.setupUi(self.MainWindow7)            #
        ###############################################

        ################ Faulty Fabric ##################
        self.app8 = QtWidgets.QApplication(sys.argv)    #
        self.MainWindow8 = QtWidgets.QMainWindow()      #
        self.ui8 = Ui_FaultyFabricWindow()              #
        self.ui8.setupUi(self.MainWindow8)              #
        #################################################

        ################ Warning Window #################
        self.app9 = QtWidgets.QApplication(sys.argv)    #
        self.MainWindow9 = QtWidgets.QMainWindow()      #
        self.ui9 = Ui_Warning_window()                  #
        self.ui9.setupUi(self.MainWindow9)              #
        icon_warning = QPixmap("./Icon/MainWindow/warning.png")
        self.ui9.warning_icon.setPixmap(icon_warning)
        #################################################
        

        
###################### İnit #################################################
    def __init__(self):                                                    
        self.camera_W_H_I=Veri_Tabani_Window.get_last_Heigt_Width()         
        self.Camera_Inf = Veri_Tabani_Window.get_last_data()                
        
        self._Camera_Serials=self.Camera_Inf[0][3].split(',') 
        self._Camera_Exposure_Time=self.Camera_Inf[0][4].split(',')
        self._Camera_Cut_Off=self.Camera_Inf[0][5]
        self._Camera_Type=self.Camera_Inf[0][6].split(',')
        self.H,self.W,self.I=self.camera_W_H_I                              
        self.zoom_impact_rate=int(self.I)                                        
        self.horizontal_value_5 = 0                                         
        self.Camera_Height=int(self.H)                                          
        self.Camera_Width = int(self.W)                                        
        # self.Camera_Exposure_Time = self._Camera_Exposure_Time             
        self.camera_1 = False                                               
        self.camera_2 = False                                               
        self.camera_3 = False                                               
        self.camera_4 = False                                               
        self.upload_path = './configs/13.46.55.txt'                         
        self.Serial_port="COM4"                                             
        self.Baud_Rate="9600"                                               
        self.Windows()                                                      
        self.Trigg_Port_Button=False                                        
        self.Non_Trigg_Port_Button=False                                    
        self.Camera_Serial = [
            str(self._Camera_Serials[0]), str(self._Camera_Serials[1]),
            str(self._Camera_Serials[2]), str(self._Camera_Serials[3])
                             ]     
        self.Camera_Exposure_Time =  [
            str(self._Camera_Exposure_Time[0]), str(self._Camera_Exposure_Time[1]),
            str(self._Camera_Exposure_Time[2]), str(self._Camera_Exposure_Time[3])
                                      ]
        self.Cameras_Type=[
            str(self._Camera_Type[0]),str(self._Camera_Type[1]),
            str(self._Camera_Type[2]), str(self._Camera_Type[3])
            ]
#############################################################################

    

    ############ MainWindow Giris ################################
    def QWindow_Login(self):                                     #
        self.MainWindow1.close()                                 #
        self.MainWindow1.show()                                  #
    ##############################################################


    ############ MainWindow Camera ###############################
    def QWindow_Camera(self):                                    #
        self.MainWindow2.close()                                 #
        self.MainWindow2.showMaximized()                         #
    ##############################################################


    ############ MainWindow VeriTabani ###########################
    def QWindow_DataBase(self):                                  #
        DC.MainWindow3.close()                                   #
        DC.MainWindow3.showMaximized()                           #
    ##############################################################

    ############ MainWindow Goster ###############################
    def QWindow_Details(self):                                   #
        self.MainWindow4.close()                                 #
        self.MainWindow4.show()                                  #
    ##############################################################

    ############ MainWindow Adminas ##############################
    def QWindow_Admin(self):                                     #
        self.MainWindow5.close()                                 #
        self.MainWindow5.show()                                  #
    ##############################################################

    ############ MainWindow Adminas ##############################
    def QWindow_Kayit(self):                                     #
        self.MainWindow7.close()                                 #
        self.MainWindow7.show()                                  #
    ##############################################################

    ############ Faulty Window >>>>>##############################
    def QWindow_Kayit(self):                                     #
        self.MainWindow8.close()                                 #
        self.MainWindow8.show()                                  #
    ##############################################################

    ############ Warning Window >>>>>##############################
    def QWarning_Window(self):                                     #
        self.MainWindow9.close()                                 #
        self.MainWindow9.show()                                  #
    ##############################################################

    ########################################## FeedBacks ##########################################################################
    def FeedBack_SetupUi(self) : return self.ui1, self.ui2, self.ui3, self.ui4, self.ui5                                          #
    def FeedBack_Windows(self) : return self.MainWindow1, self.MainWindow2, self.MainWindow3, self.MainWindow4, self.MainWindow5  #
    def FeedBack_App(self) : return self.app1,self.app2,self.app3,self.app4, self.app5                                            #
    def FeedBack_Zoom_Rate(self) : return self.zoom_impact_rate                                                                   #
    def FeedBack_Port_UI(self) : return self.ui6, self.MainWindow6, self.app6                                                     #
    def Feedback_Kayt_UI(self) : return self.ui7, self.MainWindow7, self.app7                                                     #
    def Feedback_Faulty_UI(self): return self.ui8, self.MainWindow8, self.app8
    def FeedBack_Warning_UI(self): return self.ui9, self.MainWindow9, self.app9
    ########################################## FeedBacks ##########################################################################

    def Cam_out_file_folder(self):
        obj = os.scandir("./")
        for obj1 in obj:
            if obj1.is_dir() or obj1.is_file():
                if obj1.name=="Cam Out":
                    print()
                else:
                    try:
                        os.mkdir("./Cam Out")
                        os.mkdir("./Cam Out/Cam I")
                        os.mkdir("./Cam Out/Cam II")
                        os.mkdir("./Cam Out/Cam III")
                        os.mkdir("./Cam Out/Cam IV")
                    except:
                        print()
    ########################################## FeedBacks ######################################################
    def zoom_value_1(self):                                                                                   #
        self.ui2.horizontalSlider.setMaximum(self.horizontal_value_5)                                         #
        self.ui2.horizontalSlider.setMinimum(- self.horizontal_value_5)                                       #
        self.horizontal_value_1=self.ui2.horizontalSlider.value()                                             #
        if self.horizontal_value_1>=1:                                                                        #
            self.ui2.label_4.setText(str(self.horizontal_value_1*self.zoom_impact_rate))                      #
        else:                                                                                                 #
            self.ui2.label_4.setText("Sag")                                                                   #
        return self.horizontal_value_1*self.zoom_impact_rate                                                  #
                                                                                                              #
    def zoom_value_3(self):                                                                                   #
                                                                                                              # 
        self.ui2.horizontalSlider_3.setMaximum(int((self.horizontal_value_5*self.zoom_impact_rate/int(self.Camera_Width)*self.Camera_Height))) #      
        self.ui2.horizontalSlider_3.setMinimum(-int((self.horizontal_value_5*self.zoom_impact_rate/int(self.Camera_Width)*self.Camera_Height)))#  
        self.horizontal_value_3=self.ui2.horizontalSlider_3.value()                                           #
                                                                                                              #
        self.ui2.label_12.setText(str(self.horizontal_value_3))                                               #
                                                                                                              #
                                                                                                              #
        return self.horizontal_value_3                                                                        #
                                                                                                              #
    def zoom_value_5(self):                                                                                   #
        self.ui2.horizontalSlider_5.setMaximum(int((int(int(self.Camera_Width/2)-1)/self.zoom_impact_rate)))                   #      
        self.ui2.horizontalSlider_5.setMinimum(0)                                                             #
        self.horizontal_value_5=self.ui2.horizontalSlider_5.value()                                           #
        if self.horizontal_value_5>=1:                                                                        #
            self.ui2.label_14.setText(str(self.horizontal_value_5*self.zoom_impact_rate))                     #
        else:                                                                                                 #
            self.ui2.label_14.setText("Yakınlaştır")                                                          #######################
        return  (int(self.horizontal_value_5*self.zoom_impact_rate), int((self.horizontal_value_5*self.zoom_impact_rate/int(int(self.Camera_Width)))*self.Camera_Height)) #                                                               #
                                                                                                                                    #                       
    #################################################################################################################################
    
    
    #####################################################################################################
    def set_config(self, config):                                                                       #
        self.ui2.horizontalSlider.setValue( int(config['value1'] / self.zoom_impact_rate) )             #
        self.ui2.horizontalSlider_3.setValue( int(config['value3'] / self.zoom_impact_rate) )           #
        self.ui2.horizontalSlider_5.setValue( int(config['value5'][0] / self.zoom_impact_rate) )        #
    #####################################################################################################

    #####################################################################################################
    def handle_change(self, config):                                                                    #
        self.set_config(config)                                                                         #
    #####################################################################################################

    #####################################################################################################
    def getFile(self):                                                                                  # 
        self.OpenFile = 0                                                                               #
        self.mode=self.OpenFile                                                                         #
        self.browser_mode = self.mode                                                                   # 
        self.filter_name = 'All files (*.*)'                                                            #
        self.dirpath = QDir.currentPath()                                                               #
        self.filepaths = []                                                                             #
        if self.browser_mode == self.OpenFile:                                                          #
            self.filepaths.append(QFileDialog.getOpenFileName(caption='Choose File',                    #
                                                    directory=self.dirpath,                             #
                                                    filter=self.filter_name)[0])                        #
        else:                                                                                           #
            self.options = QFileDialog.Options()                                                        #
            if sys.platform == 'darwin':                                                                #
                options |= QFileDialog.DontUseNativeDialog                                              #
            self.filepaths.append(QFileDialog.getSaveFileName( caption='Save/Save As',                  #
                                                    directory=self.dirpath,                             #
                                                    filter=self.filter_name,                            #
                                                    options=self.options)[0])                           #
        if len(self.filepaths) == 0:                                                                    #
            return                                                                                      #
        elif len(self.filepaths) == 1:                                                                  #
            self.ui5.lineEdit_Model.setText(str(self.filepaths[0]))                                     #
            self.Path=str(self.filepaths[0])                                                            #
    #####################################################################################################

    #####################################################################################################
    def Import_Model(self):                                                                             #
        if self.ui5.lineEdit_Model.text().split('/')[-1].split('.')[-1]!="pt":                          #
            print("Başarısız, lütfen sonu .pt ile biten bir dosya seçiniz...")                          #
            self.ui5.statusbar.showMessage(" " * 1 + "Başarısız, lütfen sonu .pt ile biten bir dosya seçiniz..." , 1500)
        else:                                                                                           #
            self.Model_Path=str(self.filepaths[0])                                                      #
            print("Başarılı")                                                                           #
            self.ui5.statusbar.showMessage(" " * 1 + "Yapay zeka import'u başarılı..." , 1500)
            Veri_Tabani_Window.set_last_model_path(self.Model_Path)                                     #
    #####################################################################################################
    def feedback_Model_Filepath(self):return self.Model_Path                                            #
    #####################################################################################################
                                                
    #####################################################################################################                                            
    def Import_Height(self):                                                                            #
        if self.ui5.lineEdit_Camera_Height.text() and int(self.ui5.lineEdit_Camera_Height.text())>=50:  #
            self.Camera_Height=int(self.ui5.lineEdit_Camera_Height.text())                                   #
            print(self.Camera_Height)                                                                   #
            print("Başarılı")                                                                           #
            self.ui5.statusbar.showMessage(" " * 1 + "Kamera yükseklik paramatresi başarılı bir şekilde import edilmiştir..." , 1500)

        else:                                                                                           #
            self.Camera_Height= 256                                                                      #
            print("Başarısız... Default 256 olarak ayarlanmıştır...")                                   #
            self.ui5.statusbar.showMessage(" " * 1 + "Kamera yükseklik paramatresi yüklenirken bir hata oluştu. Özellik 256 olarak ayarlanmıştır..." , 1500)

    def feedback_Import_Height(self):return int(self.Camera_Height)                                          #
    #####################################################################################################

    #############################################################################################################################################################
    def Import_Width(self):                                                                                                                                     #
        if self.ui5.lineEdit_Camera_Width.text() and int(self.ui5.lineEdit_Camera_Width.text())>=50 and int(self.ui5.lineEdit_Camera_Width.text()) % 32 == 0:   #
            self.Camera_Width = int(self.ui5.lineEdit_Camera_Width.text())                                                                                           #
            print(int(self.Camera_Width))                                                                                                                            #
            self.ui5.statusbar.showMessage(" " * 1 + "Kamera genişlik paramatresi başarılı bir şekilde import edilmiştir..." , 1500)
        else:                                                                                                                                                   #
            self.Camera_Width = 4096                                                                                                                            #
            self.ui5.statusbar.showMessage(" " * 1 + "Kamera genişlik paramatresi yüklenirken bir hata oluştu. Özellik 2592 olarak ayarlanmıştır..." , 1500)
            print("Başarısız... Default 2592 olarak ayarlanmıştır...")                                                                                          #
    #############################################################################################################################################################
    def feedback_Import_Width(self):return int(int(self.Camera_Width))                                                                                                    #
    #############################################################################################################################################################



    def Import_Serial_Port(self):
        self.Serial_port=self.ui5.combo_port.currentText()
        self.Baud_Rate=self.ui5.combo_baudrate.currentText()
        self.ui5.statusbar.showMessage(" " * 1 + "Serial port import'u başarılı bir şekilde import edilmiştir..." , 1500)
        print("Serial port import'u başarılı bir şekilde import edilmiştir...")
    def feedback_Import_Serial_Port(self):return self.Serial_port,self.Baud_Rate

    def Import_Camera_Exposure_Time(self):
        if self.ui5.radioButton_Camera_I.isChecked() == True:
            if self.ui5.lineEdit_Camera_Exposure_Time.text():
                self.Camera_Exposure_Time[0]=str(self.ui5.lineEdit_Camera_Exposure_Time.text())
                self.ui5.statusbar.showMessage(" " * 1 + "Kamera I Exposure time import'u başarılı bir şekilde import edilmiştir..." , 1500)
                return self.Camera_Exposure_Time[0]
            else:
                self.Camera_Exposure_Time[0] = "20000"
                self.ui5.statusbar.showMessage(" " * 1 + "Kamera I Exposure time import'u başarısız olmuştur. 20.000 olarak ayarlanmıştır...." , 1500)
                return self.Camera_Exposure_Time[0]
        if self.ui5.radioButton_Camera_II.isChecked() == True:
            if self.ui5.lineEdit_Camera_Exposure_Time.text():
                self.Camera_Exposure_Time[1]=str(self.ui5.lineEdit_Camera_Exposure_Time.text())
                self.ui5.statusbar.showMessage(" " * 1 + "Kamera II Exposure time import'u başarılı bir şekilde import edilmiştir..." , 1500)
                return self.Camera_Exposure_Time
            else:
                self.Camera_Exposure_Time[1] = "20000"
                self.ui5.statusbar.showMessage(" " * 1 + "Kamera II Exposure time import'u başarısız olmuştur. 20.000 olarak ayarlanmıştır...." , 1500)
                return self.Camera_Exposure_Time[1]
        if self.ui5.radioButton_Camera_III.isChecked() == True:
            if self.ui5.lineEdit_Camera_Exposure_Time.text():
                self.Camera_Exposure_Time[2]=str(self.ui5.lineEdit_Camera_Exposure_Time.text())
                self.ui5.statusbar.showMessage(" " * 1 + "Kamera III Exposure time import'u başarılı bir şekilde import edilmiştir..." , 1500)
                return self.Camera_Exposure_Time[2]
            else:
                self.Camera_Exposure_Time[2] = "20000"
                self.ui5.statusbar.showMessage(" " * 1 + "Kamera III Exposure time import'u başarısız olmuştur. 20.000 olarak ayarlanmıştır...." , 1500)
                return self.Camera_Exposure_Time[2]
        if self.ui5.radioButton_Camera_III.isChecked() == True:
            if self.ui5.lineEdit_Camera_Exposure_Time.text():
                self.Camera_Exposure_Time[3]=str(self.ui5.lineEdit_Camera_Exposure_Time.text())
                self.ui5.statusbar.showMessage(" " * 1 + "Kamera IV Exposure time import'u başarılı bir şekilde import edilmiştir..." , 1500)
                return self.Camera_Exposure_Time[3]
            else:
                self.Camera_Exposure_Time[3] = "20000"
                self.ui5.statusbar.showMessage(" " * 1 + "Kamera IV Exposure time import'u başarısız olmuştur. 20.000 olarak ayarlanmıştır...." , 1500)
                return self.Camera_Exposure_Time[3]
        print(self.Camera_Exposure_Time)
    def feedback_Import_Exposure_Time(self, index): return int(self.Camera_Exposure_Time[index])      
    def Import_Camera_Serial(self):
        if self.ui5.radioButton_Camera_I.isChecked() == True:
            if self.ui5.lineEdit_Camera_Serial.text():
                self.Camera_Serial[0]=str(self.ui5.lineEdit_Camera_Serial.text())
                self.ui5.statusbar.showMessage(" " * 1 + "Kamera serial import'u başarılı olmuştur..." , 1500)
                return self.Camera_Serial
            else:
                self.Camera_Serial[0] = "40113345"
                self.ui5.statusbar.showMessage(" " * 1 + "Kamera serial import'u başarısız olmuştur. '40113345' olarak ayarlandı" , 1500)
                return self.Camera_Serial
        if self.ui5.radioButton_Camera_II.isChecked() == True:
            if self.ui5.lineEdit_Camera_Serial.text():
                self.Camera_Serial[1]=str(self.ui5.lineEdit_Camera_Serial.text())
                self.ui5.statusbar.showMessage(" " * 1 + "Kamera serial import'u başarılı olmuştur..." , 1500)
                return self.Camera_Serial
            else:
                self.Camera_Serial[1] = "40113349"
                self.ui5.statusbar.showMessage(" " * 1 + "Kamera serial import'u başarısız olmuştur. '40113349' olarak ayarlandı" , 1500)
                return self.Camera_Serial
        if self.ui5.radioButton_Camera_III.isChecked() == True:
            if self.ui5.lineEdit_Camera_Serial.text():
                self.Camera_Serial[2]=str(self.ui5.lineEdit_Camera_Serial.text())
                self.ui5.statusbar.showMessage(" " * 1 + "Kamera serial import'u başarılı olmuştur..." , 1500)
                return self.Camera_Serial
            else:
                self.Camera_Serial[2] = "40174977"
                self.ui5.statusbar.showMessage(" " * 1 + "Kamera serial import'u başarısız olmuştur. '40174977' olarak ayarlandı" , 1500)
                return self.Camera_Serial
        if self.ui5.radioButton_Camera_IV.isChecked() == True:
            if self.ui5.lineEdit_Camera_Serial.text():
                self.Camera_Serial[3]=str(self.ui5.lineEdit_Camera_Serial.text())
                self.ui5.statusbar.showMessage(" " * 1 + "Kamera serial import'u başarılı olmuştur..." , 1500)
                return self.Camera_Serial
            else:
                self.Camera_Serial[3] = "40113349"
                self.ui5.statusbar.showMessage(" " * 1 + "Kamera serial import'u başarısız olmuştur. '40113349' olarak ayarlandı" , 1500)
                return self.Camera_Serial
        print(self.Camera_Serial)

    def Import_Cameras_Type(self):
        if self.ui5.radioButton_Camera_I.isChecked():
            self.Cameras_Type[0]=self.ui5.comboBox.currentText()
        else:
            self.Cameras_Type[0]="Alan Kamera"
        if self.ui5.radioButton_Camera_II.isChecked():
            self.Cameras_Type[1]=self.ui5.comboBox.currentText()
        else:
            self.Cameras_Type[1]="Alan Kamera"
        if self.ui5.radioButton_Camera_III.isChecked():
            self.Cameras_Type[2]=self.ui5.comboBox.currentText()
        else:
            self.Cameras_Type[2]="Alan Kamera"
        if self.ui5.radioButton_Camera_IV.isChecked():
            self.Cameras_Type[3]=self.ui5.comboBox.currentText()
        else:
            self.Cameras_Type[3]="Alan Kamera"

    def download(self, configs, time):
        with open(f'./configs/{time}.txt', 'w') as convert_file:
            convert_file.write(json.dumps(configs))
            Veri_Tabani_Window.set_last_path(f'./configs/{time}.txt')


            
    def upload(self):
        
        self.OpenFile = 0
        self.mode=self.OpenFile
        self.browser_mode = self.mode
        self.filter_name = 'All files (*.*)'
        self.dirpath = QDir.currentPath()
        self.filepaths = []
        if self.browser_mode == self.OpenFile:
            self.filepaths.append(QFileDialog.getOpenFileName(caption='Choose File',
                                                    directory=self.dirpath,
                                                    filter=self.filter_name)[0])
        else:
            self.options = QFileDialog.Options()
            if sys.platform == 'darwin':
                options |= QFileDialog.DontUseNativeDialog
            self.filepaths.append(QFileDialog.getSaveFileName( caption='Save/Save As',
                                                    directory=self.dirpath,
                                                    filter=self.filter_name,
                                                    options=self.options)[0])

        if len(self.filepaths) == 0:
            return False

        elif len(self.filepaths) == 1:
            print(self.filepaths[-1].split('/')[-1].split('.')[-1])
            if self.filepaths[-1].split('/')[-1].split('.')[-1]=="txt":
                with open(str(self.filepaths[-1])) as f:
                    data = f.read()
                self.js = json.loads(data)
                Veri_Tabani_Window.set_last_path(str(self.filepaths[-1]))
                return True
            else:
                return False

    def feedback_js(self):
        return self.js

    def default_upload(self):
        config_path = Veri_Tabani_Window.get_last_path()
        with open(config_path) as f:
            data = f.read()
            self.js = json.loads(data)

    def Port_Op(self):
        self.Trigg_Port_Button=True
        self.Non_Trigg_Port_Button=False
        print(self.Trigg_Port_Button)
        self.ui2.statusbar.showMessage(" "*1 + " Serial Port Aktif...", 1500)
    def Port_Close(self):
        self.Trigg_Port_Button=False
        self.Non_Trigg_Port_Button=True
        print(self.Trigg_Port_Button)
        self.ui2.statusbar.showMessage(" "*1 + " Serial Port Aktif Değil...", 1500)

    def Splited_Last_Data(self):
        self._path=self.Camera_Inf[0][0]
        self._Camera_Serial=self.Camera_Inf[0][4].split(',')[0]
        self._Camera_Exposure_Time=self.Camera_Inf[0][5]
        self._Camera_Cut_Off=self.Camera_Inf[0][6]
        print(str(self._path) + str(self._Camera_Serial) + str(self._Camera_Exposure_Time) + str(self._Camera_Cut_Off))
    
    def feedback_Splited_Last_Data(self):
        return self.Camera_Height, self.Camera_Width, self.zoom_impact_rate, self.Camera_Serial, self.Camera_Exposure_Time, 20, self.Cameras_Type
       