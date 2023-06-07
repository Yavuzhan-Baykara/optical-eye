# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 08:58:17 2022

@author: kaans
"""

import cv2 
from datetime import datetime
from PyQt5.QtCore import QTimer, QTime,  QThread, pyqtSignal
from imageio import get_writer
import time
from compare import * 
from os import scandir, mkdir

from threading import Thread, Timer
from Db_Con import Veri_Tabani_Window

class Helper():
    def __init__(self, now=None):
       self.now = datetime.now()
       self.db_queue=[]
       self.stopped = False
       self.last_images = []
       self.main_path = "./" 
       self.main_pdf_path = "./PDF"

    def start(self):
        Timer(0.01,self.get_time,args=()).start()
        Thread(target=self.update_db, args=()).start()

        return self

    def get_time(self):
            self.now = datetime.now()
            Timer(0.01,self.get_time,args=()).start()
    
    def update_db(self):
        while 1:
            time.sleep(0.0001)
            if len(self.db_queue) != 0:
                task=self.db_queue.pop(0)
                Veri_Tabani_Window().Ekle(self.Db_path_time(choice="Now-Day"),task['Dok_no'] , task['Kalite_no'], task['Metre'], task['Bez_eni'], task['Duvar_metre'], task['En'], task['Boy'], task['Alan'],str(task['df'].iloc[:]['name'][task['detect']]), task['Save_image'], task['Hata_Koordinant'])
                self.db_queue.clear()
            else:
                continue
            
    def check_similarity(self, img1):
        result = False
        # if len(self.last_images) >7:
        #     del self.last_images[:4]
        for image in self.last_images:
            if compare_images(image, img1):
                result = True
        return result
            
    
    def append_db(self, df, detect, Save_image, Metre, En, Boy, Alan, Dok_no, Kalite_no, Hata_Koordinant, bez_eni, Duvar_metre):
        if len(self.db_queue) < 2:
            task ={
                'df': df,
                'detect': detect,
                'Save_image': Save_image,
                'Metre': Metre,
                'En' : En,
                'Boy': Boy,
                'Alan': Alan,
                'Dok_no': Dok_no,
                'Kalite_no': Kalite_no,
                'Hata_Koordinant': Hata_Koordinant,
                'Bez_eni': bez_eni,
                'Duvar_metre': Duvar_metre,
                }
            self.db_queue.append(task)

 
    def readVideo(self,src=3):
        day_db_is_here, writer = self.video_path_definer()
       
        if src==1:
            return  day_db_is_here, writer
        
        if src==2:
            return day_db_is_here, writer
        
       
        if src==3:
            return  day_db_is_here, writer
        
        if src==4:
            return  day_db_is_here, writer
          
    def readImages(self,src=3):
        img_save_cam_I, img_save_cam_II, img_save_cam_III, img_save_cam_IV = self.img_path_definer()
        if src==1:
            return  img_save_cam_I
        
        
        if src==2:
            return  img_save_cam_II
        
       
        if src==3:
            return  img_save_cam_III
        
        if src==4:
            return  img_save_cam_IV
       
    #WebCam sayısını bulmaya yarayan fonksiyon
    def get_cams(self):
        index = 0
        arr = []
        while True:
            cap = cv2.VideoCapture(index)
            if not cap.read()[0]:
                break
            else:
                arr.append(index)
            cap.release()
            index += 1
        return arr
    
    def video_path_definer(self):
        ##Zaman ve path uzantıları   
        # String Dönüşümü
        path_time = self.now.strftime('%H:%M:%S')
        path_cam_I="Cam Out/Cam I/videos"
        path_cam_II="Cam Out/Cam II/videos"
        path_cam_III="Cam Out/Cam III/videos"
        path_cam_IV="Cam Out/Cam IV/videos"
        #Database yolu
        day_db_is_here="./Database"
        ####CAPTURE
        fps = 25  # Hz
        time_to_record = 5  # seconds
        images_to_grab = fps * time_to_record
        writer = get_writer(
        				path_cam_III+path_time+".avi",
        				 # size [W,H]
                        macro_block_size=1,
        				fps=fps,
        				quality=None
        				)
       
        return (day_db_is_here, writer)
    def img_path_definer(self):
        path_time = self.now.strftime('%H:%M:%S')
        path_cam_I="Cam Out/Cam I/images"
        path_cam_II="Cam Out/Cam II/images"
        path_cam_III="Cam Out/Cam III/images"
        path_cam_IV="Cam Out/Cam IV/images"
        ## İmage Save Cams
        img_save_cam_I=path_cam_III+"Cam_I_"+path_time+".jpeg"
        img_save_cam_II=path_cam_III+"Cam_II_"+path_time+".jpeg"
        img_save_cam_III=path_cam_III+"Cam_III_"+path_time+".jpeg"
        img_save_cam_IV=path_cam_III+"Cam_IV_"+path_time+".jpeg"
        
        return (img_save_cam_I, img_save_cam_II, img_save_cam_III, img_save_cam_IV)
      
    def Db_path_time(self,choice=""):
        if choice=="Now-Day":
            day=self.now.day
            month=self.now.month
            year=self.now.year
            now=str(day)+"."+str(month)+"."+str(year)
            return now
        elif choice=="Now-Time":
            current_time = QTime.currentTime()
            now = current_time.toString('hh.mm.ss')
            return now
        else:
            now="00.00.00"
            return now
    def pdf_folder_create(self):
        folders = scandir(self.main_path)
        for folder in folders:
            if folder.is_dir() or folder.is_file() :
                if (folder.name == "PDF"):
                    print("PDF klasörü bulunmakta...")
                else:
                    try:
                        mkdir(self.main_pdf_path)
                        print("PDF klasörü oluşturuldu...")
                        return
                    except:
                        print("PDF klasörü oluşturuldu...")

        