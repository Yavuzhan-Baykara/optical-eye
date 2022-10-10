import serial
from time import sleep
from threading import Thread
from re import findall
class AThread:
    def __init__(self,com,bound):
        self.com = com
        self.bound = bound
        self.ser = serial.Serial(com, baudrate=bound, timeout=0)
        self.src = 0
        self._stop = False

    def stop(self):
        self._stop = True
    def start(self):
        Thread(target = self.update,args=()).start()
        return self
    def update(self):
        try:
            if self._stop == True:
                return
            while True:
                self.inp = self.ser.readline()
                self.inp = str(self.inp)
                self.inp = findall('[0-9]+', self.inp)
                if self.inp:
                    self.src = self.src + 1
                sleep(1./120)
        except:
            print("Stopped")
            return
    def read(self):
        return self.inp
    def feedbacksrc(self):
        return self.src
