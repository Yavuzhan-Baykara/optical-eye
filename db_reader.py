from threading import Thread, Timer
from Db_Con import *

class db_writer():
    def __init__(self):
       self.db_queue=[]
       print("__init__: " + str(self.db_queue))
       self.stopped = False
    def update_db_start(self):
        Thread(target=self.update_db, args=()).start()
        return self
    def update_db(self):
        while True:
            if self.db_queue:
                task=self.db_queue.pop(0)
                Veri_Tabani_Window().Ekle(self.Db_path_time(choice="Now-Day"),0 , 0, 0, 0, 0, 0, 0, 0,str(task['df'].iloc[:]['name'][task['detect']]), task['Save_image'])
                print(self.db_queue)
    def append_db(self, df, detect, Save_image):
        task ={
            'df': df,
            'detect': detect,
            'Save_image': Save_image
              }
        self.db_queue.append(task)