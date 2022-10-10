from threading import Thread
from PDF_Writer import *
from time import sleep


class PDFThread:
    def __init__(self):
        
        self._stop=False
    def stop(self):
        
        self._stop=True
        
    def start(self):
        
        Thread(target=self.update,args=()).start()
        return self
    
    def update(self):
        
        try:
            while self._stop == False:
                Data_Pre_Process().PDF_W()
                Data_Pre_Process().plt.cla()
                sleep(1./120)
                self._stop =True
        except:
            print("PDF Oluşumunda beklenmeyen bir hata")
            return