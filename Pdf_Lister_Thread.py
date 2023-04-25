from PyQt5.QtCore import QThread, pyqtSignal
from PDF_Lister import *
from time import sleep

class PDFThread_Lister(QThread):
    progress = pyqtSignal(int)
    out_path_main_signal = pyqtSignal(str)
    
    def __init__(self, Date, DateLast, mainwindow):
        super().__init__()
        self.mainwindow = mainwindow
        self.Split_Date = str(int(Date[0])) + '.' + str(int(Date[1])) + '.' + str(int(Date[2]))
        self.Split_Date_last = str(int(DateLast[0])) + '.' + str(int(DateLast[1])) + '.' + str(int(DateLast[2]))
        self.DPP = Data_Pre_Process_Lister(self.Split_Date, self.Split_Date_last)
            
    def run(self):
        self.DPP.PDF_W()
        sleep(1. / 120)
        self.progress.emit(100)
        self.out_path_main_signal.emit(self.DPP.out_path_main)

def mail_sender_Window(Date, DateLast, MainWindow12, callback=None):
    def on_pdf_processing_finished(value):
        if value == 100:
            MainWindow12.show()

    def handle_out_path_main(out_path_main):
        if callback:
            callback(out_path_main)

    MainWindow12.pdf_thread_lister = PDFThread_Lister(Date, DateLast, MainWindow12)
    MainWindow12.pdf_thread_lister.progress.connect(on_pdf_processing_finished)
    MainWindow12.pdf_thread_lister.out_path_main_signal.connect(handle_out_path_main)
    MainWindow12.pdf_thread_lister.start()


