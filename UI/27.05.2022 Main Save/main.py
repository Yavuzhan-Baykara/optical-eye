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
    cam=cv2.VideoCapture(num, cv2.CAP_DSHOW)
    while (cam.isOpened()):
        cv2.waitKey(1)
        ret, frame= cam.read()
        cv2.waitKey(1)
        frame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        height, width, channel=frame.shape
        step=channel*width
        qImg=QImage(frame.data,width,height,step,QImage.Format_RGB888)
        ui2.Camera_1.setPixmap(QPixmap.fromImage(qImg))

###############################
def displayImage():
    if ui2.Camera_comboBox.currentText()=="I. Kamera":
        Cam_open(0)
        print("I. Kamera Open")
    elif ui2.Camera_comboBox.currentText()=="II. Kamera":
        Cam_open(1)
        print("II. Kamera Open")
    elif ui2.Camera_comboBox.currentText()=="III. Kamera":
        Basler_Cam_Open_area()
        print("III. Kamera Open")
    elif ui2.Camera_comboBox.currentText()=="IV. Kamera":
        Basler_Cameras()
        print("IV. Kamera Open")
################################

def Basler_Cameras():
    converter = pylon.ImageFormatConverter()
    # converting to opencv bgr format
    converter.OutputPixelFormat = pylon.PixelType_BGR8packed
    converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned

    maxCamerasToUse = 2

    exitCode = 0

    try:

        tlFactory = pylon.TlFactory.GetInstance()

        devices = tlFactory.EnumerateDevices()
        if len(devices) == 0:
            raise pylon.RuntimeException("Kameralar Mevcut değil")

        # Create an array of instant cameras for the found devices and avoid exceeding a maximum number of devices.
        cameras = pylon.InstantCameraArray(min(len(devices), maxCamerasToUse))

        l = cameras.GetSize()

        # Create and attach all Pylon Devices.
        for i, cam in enumerate(cameras):
            cam.Attach(tlFactory.CreateDevice(devices[i])) 
            #print(cam)
            #cam.StartGrabbing(pylon.GrabStrategy_LatestImageOnly) # PROBLEM
            # Print the model name of the camera.
            print("Cihaz:  ", cam.GetDeviceInfo().GetModelName())

        cameras.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)

        # Grab c_countOfImagesToGrab from the cameras.
        while cameras.IsGrabbing():
            try:
                grabResult_1 = cameras[0].RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
            except genicam.GenericException as exp_cam_1:
                print(exp_cam_1)
            try:
                grabResult_2 = cameras[1].RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
            except genicam.GenericException as exp_cam_2:
                print(exp_cam_2)
                 
            if grabResult_1.GrabSucceeded():
                cameraContextValue = grabResult_1.GetCameraContext()


                # print("Camera ", cameraContextValue, ": ", cameras[cameraContextValue].GetDeviceInfo().GetModelName())
                
                image = converter.Convert(grabResult_1)
                img = image.GetArray()
                img=cv2.resize(img,(600,400))
                height, width, channel=img.shape
                step=channel*width
                qImg=QImage(img.data,width,height,step,QImage.Format_Grayscale8)
                ui2.Camera_1.setPixmap(QPixmap.fromImage(qImg))
                cv2.waitKey(1)
            else:
                print("Hata : ", grabResult_1.ErrorCode)
            grabResult_1.Release()
                
            if grabResult_2.GrabSucceeded():
                cameraContextValue_2 = grabResult_2.GetCameraContext()

                # print("Camera ", cameraContextValue_2, ": ", cameras[cameraContextValue_2].GetDeviceInfo().GetModelName())

                image_2 = converter.Convert(grabResult_2)
                img_2 = image_2.GetArray()
                
                height_2, width_2, channel_2=img_2.shape
                step_2=channel_2*width_2
                qImg_2=QImage(img_2.data,width_2,height_2,step_2,QImage.Format_Grayscale8)
                ui2.Camera_2.setPixmap(QPixmap.fromImage(qImg_2))
                cv2.waitKey(1)
            else:
                print("Hata : ", grabResult_2.ErrorCode)
            grabResult_2.Release()
                
        cameras.StopGrabbing()
    except genicam.GenericException as e:
        # Error handling
        print("Bir Sorun oluştu", e.GetDescription())
        exitCode = 1

##Giris Ekran Slotları        
ui1.Giris_pushButton.clicked.connect(giris)
#######################


##Camera Ekran Slotları
##Button Slotları

#ComboBox Slotları
ui2.Ac_pushButton.clicked.connect(displayImage)


sys.exit(app1.exec_())