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

from Camera import*
from Giris import*

from pypylon import pylon
from pypylon import genicam


zoom_value_now=0
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
def giris():
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
        print(height)
        
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
    ## Birinci kamera fps değişkenleri
    prev_frame_time = 0
    new_frame_time = 0
    
    ## İkinci kamera fps değişkenleri
    prev_frame_time_2 = 0
    new_frame_time_2 = 0
    


    maxCamerasToUse = 2
    exitCode = 0
    
    
    img = pylon.PylonImage()
    try:
        tlFactory = pylon.TlFactory.GetInstance()
        devices = tlFactory.EnumerateDevices()
        if len(devices) == 0:
            raise pylon.RuntimeException("Kameralar Mevcut değil")
    
        cameras = pylon.InstantCameraArray(min(len(devices), maxCamerasToUse))
        
        converter = pylon.ImageFormatConverter()    # converting to opencv bgr format
        converter.OutputPixelFormat = pylon.PixelType_BGR8packed
        converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned
        l = cameras.GetSize()
    
        for i, cam in enumerate(cameras):
            cam.Attach(tlFactory.CreateDevice(devices[i])) 
            print("Cihaz:  ", cam.GetDeviceInfo().GetModelName())


        cameras.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
        while cameras.IsGrabbing():
            3
            grabResult_III = cameras[0].RetrieveResult(10000, pylon.TimeoutHandling_ThrowException)
            grabResult_IV = cameras[1].RetrieveResult(1000, pylon.TimeoutHandling_ThrowException)
            if grabResult_III.GrabSucceeded():
                # cameraContextValue = grabResult_1.GetCameraContext()
    
    
                # print("Camera ", cameraContextValue, ": ", cameras[cameraContextValue].GetDeviceInfo().GetModelName())
                
                image = converter.Convert(grabResult_III)
                img_save = image.GetArray()
                img = image.GetArray()
                img=cv2.resize(img,(800+(zoom_value_3()*zoom_impact_rate),800+(zoom_value_3()*zoom_impact_rate)))
                height_III, width_III, channel_III=img.shape
                step_III=channel_III*width_III
                qImg=QImage(img.data,width_III,height_III,step_III,QImage.Format_Grayscale8)
                ui2.Camera_1.setPixmap(QPixmap.fromImage(qImg))
                cv2.waitKey(1)
                ##Video Kayıt
                # size_III = (width_III, height_III)
                if True:
                    print("sa")
                # if ui2.Cam_III_Record==1:
                #     print("sa")
                #     # ipo = pylon.ImagePersistenceOptions()
                #     # quality = 0
                #     # filename = "saved_pypylon_img_%d.jpeg" % quality
                #     # img.Save(pylon.ImageFileFormat_Jpeg, filename, ipo)
                #     # ui2.Cam_III_Record=0

                #################
                if ui2.logic_All==0:
                    break
                
            
            else:
                print("Hata : ", grabResult_III.ErrorCode)
            grabResult_III.Release()
            if grabResult_IV.GrabSucceeded():
                # cameraContextValue_2 = grabResult_IV.GetCameraContext()
    
                # print("Camera ", cameraContextValue_2, ": ", cameras[cameraContextValue_2].GetDeviceInfo().GetModelName())
    
                image_IV = converter.Convert(grabResult_IV)
                img_IV = image_IV.GetArray()
                img_IV=cv2.resize(img_IV,(1000+(zoom_value_4()*zoom_impact_rate),1000+(zoom_value_4()*zoom_impact_rate)))
                height_IV, width_IV, channel_IV=img_IV.shape
                step_IV=channel_IV*width_IV
                qImg_IV=QImage(img_IV.data,width_IV,height_IV,step_IV,QImage.Format_Grayscale8)
                ui2.Camera_2.setPixmap(QPixmap.fromImage(qImg_IV))
                
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
                print("Hata : ", grabResult_IV.ErrorCode)
            
            grabResult_IV.Release()    
        cameras.StopGrabbing()
    except genicam.GenericException as e:
        
        # Error handling
        print("Bir Sorun oluştu", e.GetDescription())

    

##Zoom 
def zoom_value_3():
    val=ui2.horizontalSlider_3.value()
    if val>=1:
        ui2.label_12.setText(str(val*zoom_impact_rate))
    else:
        ui2.label_12.setText("AYAR III")
    return val
##Zoom 
def zoom_value_4():
    val=ui2.horizontalSlider_4.value()
    if val>=1:
        ui2.label_13.setText(str(val*zoom_impact_rate))
    else:
        ui2.label_13.setText("AYAR IV")
    return val

##Video Kayıt



    
 
###Video Kayıt Save Kısmı
def Video_Selected():
    ui2.logic=1
    ui2.Durum_Cam.setText("AÇIK")
        
    if ui2.Camera_comboBox.currentText()=="I. Kamera":
            print()
        
    elif ui2.Camera_comboBox.currentText()=="II. Kamera":
            print()
    elif ui2.Camera_comboBox.currentText()=="III. Kamera":
        print("Video Start III")
        
    elif ui2.Camera_comboBox.currentText()=="IV. Kamera":
        ui2.Cam_III_Record=1
        ui2.logic=1
        Basler_Cameras()
        print()
        print("Video Start IV")
    
    

##Kayıt etmenin durdurulması
def Click_Button_Stop():
    ui2.logic=0
    
    ui2.Durum_Cam.setText("KAPALI")

##Bütün Kameraların Kapatılması Buttonu
def Click_Button_All_Stop():
    ui2.logic_All=0
    pixmap = QPixmap('CameraOFF.PNG')
    ui2.Camera_2.setPixmap(pixmap)
    ui2.Camera_1.setPixmap(pixmap)
    print(ui2.logic_All)    
    
## Çıkış Buttonu
def Close():
        MainWindow1.close()
        MainWindow2.close()
        
      
        
      
        
      
        
      
        
      
        
        

def main():
    MainWindow2.show()


if __name__ == '__main__':
    main()    
    
    
    
    
##Giris Ekran Slotları        
#######################


##Camera Ekran Slotları
##Button Slotları

##Cam Stop

## Cam Kayıt
ui2.Start_pushButton.clicked.connect(Video_Selected)
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