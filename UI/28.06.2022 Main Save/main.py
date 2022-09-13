"""
Main Kod bölümü

"""
import time
import sys
import os

import cv2

from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QMainWindow, QMessageBox, QTableWidgetItem,QDialog            
from PyQt5 import QtCore # timer için
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QImage,QPixmap
from PyQt5.uic import loadUi

import numpy as np
##Zamanlama
from PyQt5.QtCore import QTimer, QTime, Qt

from Camera import*
from Giris import*

from pypylon import pylon
from pypylon import genicam

from datetime import datetime
from imageio import get_writer

from Ysa import *

from Db_Con import *
import Db_Con as DC
import random



img_pylon_1 = pylon.PylonImage()
img_pylon_2 = pylon.PylonImage()
img_pylon_3 = pylon.PylonImage()
img_pylon_4 = pylon.PylonImage()

##Zaman ve path uzantıları
now=datetime.now()
current_time = QTime.currentTime()
# String Dönüşümü
Path_time = current_time.toString('hh_mm_ss')

Path_Cam_I="Cam Out/Cam I/"
Path_Cam_II="Cam Out/Cam II/"
Path_Cam_III="Cam Out/Cam III/"
Path_Cam_IV="Cam Out/Cam IV/"

## İmage Save Cams
img_save_Cam_I=Path_Cam_III+"Cam_I_"+Path_time+".jpeg"
img_save_Cam_II=Path_Cam_III+"Cam_II_"+Path_time+".jpeg"
img_save_Cam_III=Path_Cam_III+"Cam_III_"+Path_time+".jpeg"
img_save_Cam_IV=Path_Cam_III+"Cam_IV_"+Path_time+".jpeg"

#Database yolu
Day_Db_is_here="./Database"

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
###########################





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


##MainWindow Veri Tabani
def QmenuBar_Veri_tabani():
    DC.MainWindow3.close()
    DC.MainWindow3.show()

##MainWindow Camera
def QmenuBar_Camera():
    MainWindow2.close()
    MainWindow2.show()


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
    global Cam
    colors = [(255, 255, 0), (0, 255, 0), (0, 255, 255), (255, 0, 0)]
    is_cuda = len(sys.argv) > 1 and sys.argv[1] == "cuda"
    net = Ysa.build_model(is_cuda)
    start = time.time_ns()
    frame_count = 0
    total_frames = 0
    fps = -1
    
    ###############
    prev_frame_time = 0
    new_frame_time = 0
    cam=cv2.VideoCapture(num, cv2.CAP_DSHOW)
    while (cam.isOpened()):
        ret, frame= cam.read()
        frame2=frame
        cv2.waitKey(1)
        if num==0:Cam="Cam II"
        elif num==1:Cam="Cam I"
            
        frame=Detection(frame,net,frame_count,total_frames,colors,fps,frame2,Cam)
        
        frame = cv2.resize(frame, None,fx=2.3,fy=2.2,interpolation = cv2.INTER_CUBIC)
        
        qImg = QtGui.QImage(frame.data, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        ui2.Camera_1.setPixmap(QtGui.QPixmap.fromImage(qImg))

        
        
        
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
        Basler_Cameras("3")
        print("III. Kamera Open")
    elif ui2.Camera_comboBox.currentText()=="IV. Kamera":
        ui2.logic_All=1
        Basler_Cameras("4")
        print("IV. Kamera Open")
        
################################

def Basler_Cameras(secim):
    ########################################################### Detection Ön işlem
    colors = [(255, 255, 0), (0, 255, 0), (0, 255, 255), (255, 0, 0)]
    is_cuda = len(sys.argv) > 1 and sys.argv[1] == "cuda"
    net = Ysa.build_model(is_cuda)
    start = time.time_ns()
    frame_count = 0
    total_frames = 0
    fps = -1
    ##############################################################################
    
    
    
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
        converter = pylon.ImageFormatConverter()    # converting to opencv rgb format
        converter.OutputPixelFormat = pylon.PixelType_BGR8packed
        converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned
        for i, cam in enumerate(cameras):
            cam.Attach(tlFactory.CreateDevice(devices[i])) 
            print("Cihaz:  ", cam.GetDeviceInfo().GetModelName())
        cameras.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
        while cameras.IsGrabbing():
            if secim=="3":
                try:
                    grabResult_3 = cameras[0].RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
                except genicam.GenericException as exp_cam_3:
                    print(exp_cam_3)
                if grabResult_3.GrabSucceeded():
                    image_3 = converter.Convert(grabResult_3)
                    img_to_array_3 = image_3.GetArray()
                    
                    img_to_array_3_2=image_3.GetArray()
                    img_to_array_3_2=img_to_array_3_2[1500:1800, 1900:2450]
                    
                    height, width, channel=img_to_array_3.shape
                    # img_to_array_3=cv2.resize(img_to_array_3,(height-(zoom_value_3()*zoom_impact_rate)*4,width-(zoom_value_3()*zoom_impact_rate)*4))
                    img_to_array_3=img_to_array_3[1500:1800, 1900:2450]
                    
                    img_to_array_3=Detection(img_to_array_3,net,frame_count,total_frames,colors,fps,img_to_array_3_2,"Cam III")
                    
                    img_to_array_3=cv2.resize(img_to_array_3,(height+(zoom_value_3()*zoom_impact_rate)*4,width+(zoom_value_3()*zoom_impact_rate)*4))
                    height, width, channel=img_to_array_3.shape
                    step=channel*width
                    
                    
                    qImg=QImage(img_to_array_3.data,width,height,step,QImage.Format_RGB888)
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
                        img_to_array_3=cv2.cvtColor(img_to_array_3,cv2.COLOR_RGB2GRAY)
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
                        image_3 = converter.Convert(grabResult_3)
                        img_3 = image_3.GetArray()
                        img_3 = cv2.resize(img_3, None,fx=5,fy=5,interpolation = cv2.INTER_CUBIC)
                        cv2.imwrite(img_save_Cam_III,img_3)
                        # img_pylon_3.AttachGrabResultBuffer(grabResult_3)
                        # ipo = pylon.ImagePersistenceOptions()
                        # img_pylon_3.Save(pylon.ImageFileFormat_Jpeg, img_save_Cam_III, ipo)
                        ui2.Cam_III_Save=0
    #############################################################################################################
                    ##Tüm Kameraların Kapatılması
                    if ui2.logic_All==0:
                        break 
                else:
                    print("Hata : ", grabResult_3.ErrorCode)
                grabResult_3.Release()
            elif secim=="4":
                try:
                    grabResult_4 = cameras[1].RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
                except genicam.GenericException as exp_cam_4:
                    print(exp_cam_4)
                if grabResult_4.GrabSucceeded():
                    image_2 = converter.Convert(grabResult_4)
                    img_2 = image_2.GetArray()
                    img_2=cv2.resize(img_2,(1000+(zoom_value_4()*zoom_impact_rate),1000+(zoom_value_4()*zoom_impact_rate)))
                    height_2, width_2, channel_2=img_2.shape
                    step_2=channel_2*width_2
                    qImg_2=QImage(img_2.data,width_2,height_2,step_2,QImage.Format_Grayscale8)
                    ui2.Camera_1.setPixmap(QPixmap.fromImage(qImg_2))
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
    pixmap = QPixmap('./Icon/Label Img/CameraOFF.PNG')
    ui2.Camera_1.setPixmap(pixmap) 
    ui2.label_9.setText(str(0))
    Veri_Tabani_Window.Button_Show()
## Çıkış Buttonu
def Close():
    
    MainWindow1.close()
    MainWindow2.close()
    cv2.destroyAllWindows()
    ui2.logic_All=0
    pixmap = QPixmap('./Icon/Label Img/CameraOFF.PNG')
#SAAT###############################################################################################################
def showTime():
    # Şimdiki zaman Current Time
    current_time = QTime.currentTime()
    # String Dönüşümü
    label_time = current_time.toString('hh:mm:ss')
    # Label üzerinde gösterim
    ui2.label_11.setText(label_time)        
#########################################################################################################################################################################################
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

    
def New_Day_Folder():
    day=datetime.now().day
    month=datetime.now().month
    year=datetime.now().year
    now=str(day)+"."+str(month)+"."+str(year)
    obj=os.scandir(Day_Db_is_here)
    for entry in obj:
        if entry.is_dir() or entry.is_file():
            if entry.name==now:
                print("Klasör Oluşturulmuş")
            else:
                try:
                    New_Day_Create_Folder(now)
                    os.mkdir(Day_Db_is_here+"/"+now+"/"+"Cam I")
                    os.mkdir(Day_Db_is_here+"/"+now+"/"+"Cam II")
                    os.mkdir(Day_Db_is_here+"/"+now+"/"+"Cam III")
                    os.mkdir(Day_Db_is_here+"/"+now+"/"+"Cam IV")
                    break
                except:
                    print("Klasör Zaten var")
                    break
                    


def Detection(frame,net,frame_count,total_frames,colors,fps,frame_origin,Cam):
    global box,classid
    now=datetime.now()
    day=now.day
    month=now.month
    year=now.year
    hour=now.hour
    minute=now.minute
    sec=now.second
    rdm=random.uniform(0, 5)
    inputImage = Ysa.format_sp(frame)
    
    outs = Ysa.detect(inputImage, net)
    class_ids, confidences, boxes = Ysa.wrap_detection(inputImage, outs[0])
    frame_count += 1
    total_frames += 1
    
    for (classid, confidence, box) in zip(class_ids, confidences, boxes):
         color = colors[int(classid) % len(colors)]
         cv2.rectangle(frame, box, color, 2)
         cv2.rectangle(frame, (box[0], box[1] - 20), (box[0] + box[2], box[1]), color, -1)
         cv2.putText(frame, Ysa.class_list[classid], (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, .5, (0,0,0))

    if frame_count >= 30:
        end = time.time_ns()
        fps = 1000000000 * frame_count / (end - start)
        frame_count = 0
        start = time.time_ns()
    
    if int(fps) > 0:
        fps_label = "FPS: %.2f" % int(fps)
        cv2.putText(frame, fps_label, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    
    x1=box[1]
    x2=box[1]+box[3]
    y1=box[0]
    y2=box[0]+box[2]
    if(x1<=0):x1=0
    if(y1<=0):y1=0 
    if (x1<=6):x1=6
    if(y1<=6):y1=6
    
    crop=frame_origin[x1-5:x2+5,y1-5:y2+5]
    # print(str(Ysa.class_list[classid])+"_"+str(day)+"."+str(month)+"."+str(year)+"."+str(hour)+"."+str(minute)+"."+str(sec)+"_"+Cam)
    cv2.imwrite("./Database/"+str(day)+"."+str(month)+"."+str(year)+"/"+Cam+"/"+str(Ysa.class_list[classid])+"_"+str(day)+"."+str(month)+"."+str(year)+"."+str(hour)+"."+str(minute)+"."+str(sec)+"."+str(rdm)+".jpg",crop)
    now_DB=str(day)+"."+str(month)+"."+str(year)
    Path_DB="./Database/"+str(day)+"."+str(month)+"."+str(year)+"/"+Cam+"/"+str(Ysa.class_list[classid])+"_"+str(day)+"."+str(month)+"."+str(year)+"."+str(hour)+"."+str(minute)+"."+str(sec)+"."+str(rdm)+".jpg"
    Veri_Tabani_Window.Ekle(now_DB,0 , 0, 0, 0, 0, 0, 0, 0,str(Ysa.class_list[classid]), Path_DB, Cam)
    conn.commit()
    cv2.waitKey(50)
    return frame


def New_Day_Create_Folder(name):
    os.mkdir(Day_Db_is_here+"/"+name)
    


def main():
    MainWindow2.show()
    New_Day_Folder()
    Veri_Tabani_Window.Listele()

    


if __name__ == '__main__':
    main()    
    timer = QTimer()
    timer.timeout.connect(showTime)
    timer.start(1000)



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

##QMenu Bar
ui2.menuAna_Sayfa.aboutToShow.connect(QmenuBar_Veri_tabani)


## Veri Tabani Window
DC.ui3.menuCamera.aboutToShow.connect(QmenuBar_Camera)
DC.ui3.Temiz_pushButton.clicked.connect(Veri_Tabani_Window.Clear)
DC.ui3.Veri_Tabani_Widget.itemSelectionChanged.connect(Veri_Tabani_Window.Doldur)
DC.ui3.Goster_pushButton.clicked.connect(Veri_Tabani_Window.Ara)
sys.exit(app1.exec_())