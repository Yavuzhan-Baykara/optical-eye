import time

from threading import Thread
import cv2
class WebcamVideoStream:
    def __init__(self, src):
            print('SA1')
            self.src = src
            self.stream = cv2.VideoCapture(self.src, cv2.CAP_DSHOW)
            self.started = False
            (self.ret, self.frame) = self.stream.read()
            self.stopped = False
                 

                 
    def start(self):
            # start the thread to read frames from the video stream
            if self.started: 
                print("already started")
                return None
            self.started = True
            Thread(target=self.update, args=()).start()
            return self
    def update(self):
         
                
                while self.started:
                                    
                    self.ret, self.frame = self.stream.read()
                
    def read(self):
            if self.ret:
                return self.frame
    def stop(self):
            # indicate that the thread should be stopped
            self.started = False
    def finish(self):
            return False