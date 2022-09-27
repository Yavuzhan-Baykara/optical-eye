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
    
    converter = pylon.ImageFormatConverter()    # converting to opencv bgr format
    converter.OutputPixelFormat = pylon.PixelType_BGR8packed
    converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned

    maxCamerasToUse = 2

    exitCode = 0

    try:

        tlFactory = pylon.TlFactory.GetInstance()

        devices = tlFactory.EnumerateDevices()
        if len(devices) == 0:
            raise pylon.RuntimeException("Kameralar Mevcut değil")

        cameras = pylon.InstantCameraArray(min(len(devices), maxCamerasToUse))

        l = cameras.GetSize()

        for i, cam in enumerate(cameras):
            cam.Attach(tlFactory.CreateDevice(devices[i])) 

            print("Cihaz:  ", cam.GetDeviceInfo().GetModelName())

        cameras.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)

        while cameras.IsGrabbing():
            try:
                grabResult_1 = cameras[0].RetrieveResult(10000, pylon.TimeoutHandling_ThrowException)
            except genicam.GenericException as exp_cam_1:
                print(exp_cam_1)
            try:
                grabResult_2 = cameras[1].RetrieveResult(1000, pylon.TimeoutHandling_ThrowException)
            except genicam.GenericException as exp_cam_2:
                print(exp_cam_2)
                 
            if grabResult_1.GrabSucceeded():
                # cameraContextValue = grabResult_1.GetCameraContext()


                # print("Camera ", cameraContextValue, ": ", cameras[cameraContextValue].GetDeviceInfo().GetModelName())
                
                image = converter.Convert(grabResult_1)
                img = image.GetArray()
                img=cv2.resize(img,(800+(zoom_value_3()*zoom_impact_rate),800+(zoom_value_3()*zoom_impact_rate)))
                height, width, channel=img.shape
                step=channel*width
                qImg=QImage(img.data,width,height,step,QImage.Format_Grayscale8)
                ui2.Camera_1.setPixmap(QPixmap.fromImage(qImg))
                
                #Show FPS Kamera I
                
                cv2.waitKey(1)
                if ui2.logic_All==0:
                    break
                
            else:
                print("Hata : ", grabResult_1.ErrorCode)
            grabResult_1.Release()
                
            if grabResult_2.GrabSucceeded():
                cameraContextValue_2 = grabResult_2.GetCameraContext()

                # print("Camera ", cameraContextValue_2, ": ", cameras[cameraContextValue_2].GetDeviceInfo().GetModelName())

                image_2 = converter.Convert(grabResult_2)
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
                print("Hata : ", grabResult_2.ErrorCode)
            grabResult_2.Release()
                
        cameras.StopGrabbing()
    except genicam.GenericException as e:
        # Error handling
        print("Bir Sorun oluştu", e.GetDescription())
        exitCode = 1

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

def Video_Start_Save_Demo(num):
    cam=cv2.VideoCapture(num, cv2.CAP_DSHOW)
    frame_width = int(cam.get(3))
    frame_height = int(cam.get(4))
   
    size = (frame_width, frame_height)
    result = cv2.VideoWriter('filename2.avi', 
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         10, size)
    
    while (cam.isOpened()):
        ret, frame= cam.read()
        result.write(frame)
        cv2.imshow('frame',frame)
        cv2.waitKey(1)
        if ui2.logic==0:
            break
            
    cam.release()
    result.release()
    cv2.destroyAllWindows()
    
 
###Video Kayıt Save Kısmı
def Video_Selected():
    ui2.logic=1
    ui2.Durum_Cam.setText("AÇIK")
        
    if ui2.Camera_comboBox.currentText()=="I. Kamera":
        Video_Start_Save_Demo(0)
    elif ui2.Camera_comboBox.currentText()=="II. Kamera":
        Video_Start_Save_Demo(1)
    elif ui2.Camera_comboBox.currentText()=="III. Kamera":
        print("Video Start III")
        
    elif ui2.Camera_comboBox.currentText()=="IV. Kamera":
        Basler_Cameras()
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