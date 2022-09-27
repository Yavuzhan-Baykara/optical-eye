from threading import Thread
from PDF_Lister import *
from time import sleep



class PDFThread_Lister:
    def __init__(self, Date, DateLast):
        
        self._stop=False
        
        self.Split_Date=str(int(Date[0]))+'.'+str(int(Date[1]))+'.'+str(int(Date[2]))
        self.Split_Date_last=str(int(DateLast[0]))+'.'+str(int(DateLast[1]))+'.'+str(int(DateLast[2]))
        self.DPP=Data_Pre_Process_Lister(self.Split_Date, self.Split_Date_last)

    def stop(self):
        
        self._stop=True
        
    def start(self):
        
        Thread(target=self.update,args=()).start()
        return self
    
    def update(self):
            while self._stop == False:
                self.DPP.PDF_W()
                sleep(1./120)
                self._stop =True
                

