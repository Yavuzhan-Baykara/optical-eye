"""
Main Kod bölümü

"""
import time
import sys
import cv2

from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QMainWindow, QMessageBox, QTableWidgetItem,QDialog            
from PyQt5 import QtCore # timer için
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QImage,QPixmap
from PyQt5.uic import loadUi

##Zamanlama
from PyQt5.QtCore import QTimer, QTime, Qt

from Camera import*
from Giris import*

from pypylon import pylon
from pypylon import genicam

from datetime import datetime
from imageio import get_writer


img_pylon_1 = pylon.PylonImage()
img_pylon_2 = pylon.PylonImage()
img_pylon_3 = pylon.PylonImage()
img_pylon_4 = pylon.PylonImage()

##Zaman ve path uzantıları
now=datetime.now()
Path_Cam_I="Cam Out/Cam I/"
Path_Cam_II="Cam Out/Cam II/"
Path_Cam_III="Cam Out/Cam III/"
Path_Cam_IV="Cam Out/Cam IV/"

## İmage Save Cams
img_save_Cam_I=Path_Cam_III+"Cam_I_"+now.strftime("%H_%M_%S")+".jpeg"
img_save_Cam_II=Path_Cam_III+"Cam_II_"+now.strftime("%H_%M_%S")+".jpeg"
img_save_Cam_III=Path_Cam_III+"Cam_III_"+now.strftime("%H_%M_%S")+".jpeg"
img_save_Cam_IV=Path_Cam_III+"Cam_IV_"+now.strftime("%H_%M_%S")+".jpeg"


####CAPTURE
fps = 25  # Hz
time_to_record = 5  # seconds
images_to_grab = fps * time_to_record
writer = get_writer(
				Path_Cam_III+now.strftime("%H_%M_%S")+".avi",
				 # size [W,H]
                macro_block_size=1,
				fps=fps,
				quality=None
				)
zoom_impact_rate=10


####### Giris #######
app1=QtWidgets.QApplication(sys.argv)
MainWindow1=QtWidgets.QMainWindow()
ui1= Ui_Giris_Window()
ui1.setupUi(MainWindow1)
MainWindow1.show()
####### ----- #######



####### Camera ######
app2=QtWidgets.QApplication(sys.argv)
MainWindow2=QtWidgets.QMainWindow()
ui2=Ui_Camera_Window()
ui2.setupUi(MainWindow2)
####### ----- #######


    
####### Giris Doğrulaması #######
def Login():
    global name
    name=ui1.Kullaniciadi_lineEdit.text()
    password=ui1.Sifre_lineEdit.text()
    
    if(name=="yavzan" and password=='123'):
        print("Giriş Başarılı")
        MainWindow1.close()
        MainWindow2.show()
################################     

#########Camera#################
def Cam_open(num):
    ###############
    prev_frame_time = 0
    new_frame_time = 0
    cam=cv2.VideoCapture(num, cv2.CAP_DSHOW)
    while (cam.isOpened()):
        ret, frame= cam.read()
        cv2.waitKey(1)
        frame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        height, width, channel=frame.shape
        step=channel*width
        qImg=QImage(frame.data,width,height,step,QImage.Format_RGB888)
        ui2.Camera_1.setPixmap(QPixmap.fromImage(qImg))
        
        if ui2.Cam_I_Record==1:
            Cap_Path_Cam_I=Path_Cam_I+now.strftime("%H_%M_%S")+".jpg"
            cv2.imwrite(Cap_Path_Cam_I,frame)
            ui2.Cam_I_Record_isOpen=1
            UiComponents()
            
        elif ui2.Cam_I_Record==0:
            if ui2.Cam_I_Record_isOpen==1:
                ui2.Cam_I_Record_isOpen=0
                break
                
            
        
        #Show FPS Kamera Self
        new_frame_time = time.time()
        fps = 1/(new_frame_time-prev_frame_time)
        prev_frame_time = new_frame_time
        fps = int(fps)
        fps=str(fps)
        ui2.label_8.setText(fps)
        if ui2.logic_All==0:
            break
    cam.release()

###############################
def displayImage():
    if ui2.Camera_comboBox.currentText()=="I. Kamera":
        ui2.logic_All=1
        Cam_open(0)
        print("I. Kamera Open")
    elif ui2.Camera_comboBox.currentText()=="II. Kamera":
        ui2.logic_All=1
        Cam_open(1)
        print("II. Kamera Open")
    elif ui2.Camera_comboBox.currentText()=="III. Kamera":
        ui2.logic_All=1
        Basler_Cameras()
        print("III. Kamera Open")
    elif ui2.Camera_comboBox.currentText()=="IV. Kamera":
        ui2.logic_All=1
        Basler_Cameras()
        print("IV. Kamera Open")
        
################################

def Basler_Cameras():
    
    
    
    ## Üçüncü kamera fps değişkenleri
    prev_frame_time_3 = 0
    new_frame_time_3 = 0
    
    ## Dördüncü kamera fps değişkenleri
    prev_frame_time_4 = 0
    new_frame_time_4 = 0
    


    maxCamerasToUse = 2 
    exitCode = 0


    try:
        tlFactory = pylon.TlFactory.GetInstance()
        devices = tlFactory.EnumerateDevices()
        if len(devices) == 0:
            raise pylon.RuntimeException("Kameralar Mevcut değil")
    
        cameras = pylon.InstantCameraArray(min(len(devices), maxCamerasToUse))
        
        converter = pylon.ImageFormatConverter()    # converting to opencv bgr format
    
    
        converter.OutputPixelFormat = pylon.PixelType_BGR8packed
        converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned
    
        for i, cam in enumerate(cameras):
            cam.Attach(tlFactory.CreateDevice(devices[i])) 
            print("Cihaz:  ", cam.GetDeviceInfo().GetModelName())


        cameras.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
        while cameras.IsGrabbing():
            try:
                grabResult_3 = cameras[0].RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
            except genicam.GenericException as exp_cam_3:
                print(exp_cam_3)
            try:
                grabResult_4 = cameras[1].RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
            except genicam.GenericException as exp_cam_4:
                print(exp_cam_4)
            
            if grabResult_3.GrabSucceeded():
                
                image_3 = converter.Convert(grabResult_3)
                img_to_array_3 = image_3.GetArray()
                img_to_array_3=cv2.resize(img_to_array_3,(800+(zoom_value_3()*zoom_impact_rate),800+(zoom_value_3()*zoom_impact_rate)))
                height, width, channel=img_to_array_3.shape
                step=channel*width
                qImg=QImage(img_to_array_3.data,width,height,step,QImage.Format_Grayscale8)
                ui2.Camera_1.setPixmap(QPixmap.fromImage(qImg))
                cv2.waitKey(1)
                
                
#Show FPS Kamera I#############################################################################################################
                new_frame_time_3 = time.time()
                fps_3 = 1/(new_frame_time_3-prev_frame_time_3)
                prev_frame_time_3 = new_frame_time_3
                fps_3 = int(fps_3)
                fps_3=str(fps_3)
                ui2.label_8.setText(fps_3)
#############################################################################################################
                
                
                
#VİDEO KAYIT III##########################################################################################
                if ui2.Cam_III_Record==1:
                    img_to_array_3=cv2.cvtColor(img_to_array_3,cv2.COLOR_BGR2GRAY)
                    writer.append_data(img_to_array_3)
                    grabResult_3.Release()
                elif ui2.Cam_III_Record==0:
                    if ui2.Cam_III_Record_isOpen==1:
                        cv2.destroyAllWindows()
                        ui2.Cam_III_Record_isOpen=0
                        ui2.Cam_III_Record=0
                        cameras[0].StopGrabbing()
                        break
#############################################################################################################
#RESİM KAYIT III ###############################################################################################################
                if ui2.Cam_III_Save==1:
                    img_pylon_3.AttachGrabResultBuffer(grabResult_3)
                    ipo = pylon.ImagePersistenceOptions()
                    img_pylon_3.Save(pylon.ImageFileFormat_Jpeg, img_save_Cam_III, ipo)
                    ui2.Cam_III_Save=0

#############################################################################################################
                ##Tüm Kameraların Kapatılması
                if ui2.logic_All==0:
                    break
                
            else:
                print("Hata : ", grabResult_3.ErrorCode)
            grabResult_3.Release()

            if grabResult_4.GrabSucceeded():

                image_2 = converter.Convert(grabResult_4)
                img_2 = image_2.GetArray()
                img_2=cv2.resize(img_2,(1000+(zoom_value_4()*zoom_impact_rate),1000+(zoom_value_4()*zoom_impact_rate)))
                height_2, width_2, channel_2=img_2.shape
                step_2=channel_2*width_2
                qImg_2=QImage(img_2.data,width_2,height_2,step_2,QImage.Format_Grayscale8)
                ui2.Camera_2.setPixmap(QPixmap.fromImage(qImg_2))
                
                #Show FPS Kamera II
                # new_frame_time_2 = time.time()
                # fps = 1/(new_frame_time_2-prev_frame_time_2)
                # prev_frame_time = new_frame_time_2
                # fps = int(fps)
                # fps=str(fps)
                # ui2.label_8.setText(fps)

                cv2.waitKey(1)
                if ui2.logic_All==0:
                    break
            else:
                print("Hata : ", grabResult_4.ErrorCode)
            grabResult_4.Release()
                
        cameras.StopGrabbing()
    except genicam.GenericException as e:
        # Error handling
        print("Bir Sorun oluştu", e.GetDescription())

##Zoom 
def zoom_value_3():
    horizontal_value_3=ui2.horizontalSlider_3.value()
    if horizontal_value_3>=1:
        ui2.label_12.setText(str(horizontal_value_3*zoom_impact_rate))
    else:
        ui2.label_12.setText("AYAR III")
    return horizontal_value_3
##Zoom 
def zoom_value_4():
    horizontal_value_4=ui2.horizontalSlider_4.value()
    if horizontal_value_4>=1:
        ui2.label_13.setText(str(horizontal_value_4*zoom_impact_rate))
    else:
        ui2.label_13.setText("AYAR IV")
    return horizontal_value_4

##Video Kayıt



    
 
###Video Kayıt Save Kısmı
def Video_Selected():
    ui2.Durum_Cam.setText("AÇIK")
    if ui2.Camera_comboBox.currentText()=="I. Kamera":
        ui2.Cam_I_Record=1
        print("Video Start I")
        
     
    elif ui2.Camera_comboBox.currentText()=="II. Kamera":
        ui2.Cam_II_Record=1
        print("Video Start II")
        
    elif ui2.Camera_comboBox.currentText()=="III. Kamera":
        ui2.Cam_III_Record=1
        print("Video Start III")
        
    elif ui2.Camera_comboBox.currentText()=="IV. Kamera":
        ui2.Cam_IV_Record=1
        print("Video Start IV")
    
def Pic_Selected():
    if ui2.Camera_comboBox.currentText()=="I. Kamera":
        ui2.Cam_I_Save=1
    elif ui2.Camera_comboBox.currentText()=="II. Kamera":
        ui2.Cam_II_Save=1
    elif ui2.Camera_comboBox.currentText()=="III. Kamera":
        ui2.Cam_III_Save=1
    elif ui2.Camera_comboBox.currentText()=="IV. Kamera":
        ui2.Cam_IV_Save=1
##Kayıt etmenin durdurulması
def Click_Button_Stop():
    ui2.Cam_I_Record=0
    ui2.Cam_II_Record=0
    ui2.Cam_III_Record=0
    ui2.Cam_IV_Record=0
    ui2.Durum_Cam.setText("KAPALI")

##Bütün Kameraların Kapatılması Buttonu
def Click_Button_All_Stop():
    ui2.logic_All=0
    pixmap = QPixmap('CameraOFF.PNG')
    ui2.Camera_2.setPixmap(pixmap)
    ui2.Camera_1.setPixmap(pixmap) 
    ui2.label_9.setText(str(0))
## Çıkış Buttonu
def Close():
        MainWindow1.close()
        MainWindow2.close()
        
      
        
      
#SAAT###############################################################################################################
def showTime():
    # Şimdiki zaman Current Time
    current_time = QTime.currentTime()
    # String Dönüşümü
    label_time = current_time.toString('hh:mm:ss')
    # Label üzerinde gösterim
    ui2.label_11.setText(label_time)        
#########################################################################################################################################################################################

#Timer Bağlantıları############################################################################################################### 
def timer_Lab():
    timer = QTimer()
    timer.timeout.connect(showTime)
    timer.start(1000)
          
###############################################################################################################

def UiComponents():
    Start()
    timer = QTimer()
    Show_Record_Time()
    timer.timeout.connect(Show_Record_Time)
    timer.start(10)

def Show_Record_Time():
    if ui2.flag:
        ui2.count+= 1
    ui2.text = str(ui2.count / 20)
    ui2.label_9.setText(ui2.text)
    
  
  
def Start():
    ui2.flag = True
    
    
def Re_set():
    ui2.flag = False
    ui2.count = 0
    ui2.label_9.setText(str(ui2.count))    
  

        

def main():
    MainWindow2.show()
    timer_Lab()






if __name__ == '__main__':
    main()    
    timer_Lab()
    
    
    
    
    
    
##Giris Ekran Slotları        
#######################


##Camera Ekran Slotları
##Button Slotları

##Cam Stop

## Cam Kayıt
ui2.Start_pushButton.clicked.connect(Video_Selected)
##Cam Pic Save
ui2.Kayit_pushButton_2.clicked.connect(Pic_Selected)
## Cam Stop
ui2.Stop_pushButton.clicked.connect(Click_Button_Stop)
## Bütün Cam_Stop
ui2.Off_pushButton.clicked.connect(Click_Button_All_Stop)
## Exit Button
ui2.Close_pushButton.clicked.connect(Close)
#ComboBox Slotları
ui2.Ac_pushButton.clicked.connect(displayImage)


#HorizontalSlider
ui2.horizontalSlider_3.valueChanged.connect(zoom_value_3)
ui2.horizontalSlider_4.valueChanged.connect(zoom_value_4)
sys.exit(app1.exec_())