
import time
import torch
from pypylon import pylon
import matplotlib.pyplot as plt
import imutils
import PIL
import torchvision.transforms as T
from threading import Thread
import cv2
from Db_Con import *
class Active_Camera:
    def __init__(self, cam, converter, Tools, MinCamerasSize):
        
        self.camera = cam
        self.model_name = cam.GetDeviceInfo().GetSerialNumber()
        
        if self.model_name == Tools.Camera_Serial[0] or self.model_name == Tools.Camera_Serial[1]:
            self.camera_W_H_I=Veri_Tabani_Window.get_last_Heigt_Width()
            Width, Height, Rate=self.camera_W_H_I
            self.camera.Width = MinCamerasSize
            self.camera.Width = int(Tools.feedback_Import_Width())

            self.camera.Height = Height
            self.camera.Height = int(Tools.feedback_Import_Height())
            for index in range(len(Tools.Camera_Serial)):
                if Tools.Cameras_Type[index] == "Alan Kamera":
                    if self.model_name == Tools.Camera_Serial[index]: 
                        try:
                            self.camera.ExposureTime.SetValue(int(Tools.feedback_Import_Exposure_Time(index)))
                            self.camera.CenterY = True
                        except:
                            print("Alan Kameraların Exposure Timlerı düzgün ayarlanamamaştır...")
                if Tools.Cameras_Type[index] == "Çizgi Kamera":
                    if self.model_name == Tools.Camera_Serial[index]: 
                        try:
                            self.camera.ExposureTimeRaw.SetValue(int(Tools.feedback_Import_Exposure_Time(index)))
                        except:
                            print("Çizgi Kameraların Exposure Timlerı düzgün ayarlanamamaştır...")    
                            
        cam.StartGrabbing(pylon.GrabStrategy_LatestImageOnly) 
        self.converter = converter
    def calculate(self):
        if self.camera.IsGrabbing():
            self.grabResult = self.camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
            self.frame = self.converter.Convert(self.grabResult).GetArray()
class PylonVideoStream:
    def __init__(self, cameras,Tools):
          self.cameras = cameras 
          self.cameras.Open()
          self.num_of_cam = cameras.GetSize()
          self.Active_cameras = []
          self.converter = pylon.ImageFormatConverter()
          self.converter.OutputPixelFormat = pylon.PixelType_BGR8packed
          self.converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned
          self.cnt=0
          self.MinCamerasWidthArray=[]
          self.MinSizeCameras=0
          for cam in cameras:
            self.MinCamerasWidthArray.append(cam.Width.GetValue())
          self.MinSizeCameras=min(self.MinCamerasWidthArray)

          for cam in cameras:
            new_active_camera = Active_Camera(cam, self.converter, Tools, self.MinSizeCameras)
            new_active_camera.calculate()
            if new_active_camera.model_name == Tools.Camera_Serial[self.cnt]:
                self.Active_cameras.append(new_active_camera)   
            self.cnt=self.cnt+1
          self.stopped = False
          self.cnt=0
          
    def start(self):
        Thread(target=self.update, args=()).start()
        return self
        
    def update(self):
        while self.stopped == False:
            for active_cam in self.Active_cameras:
                active_cam.calculate()

    def read(self):
            frames = []
            for active_cam in self.Active_cameras:
                
                frames.append((active_cam.frame, active_cam.model_name))

            return frames
    def stop(self):
        self.cameras.Close()
        self.stopped = True