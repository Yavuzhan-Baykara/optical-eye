# example of one producer and one consumer with threads
from time import sleep
from random import random
from threading import Thread
from queue import Queue
from Db_Con import *
class Cops:
    def __init__(self):
        self.queue=(None,None,None)


    def tupple(self,df,detect,Save_image):
        self.tup=(df,detect,Save_image)

        
    # producer task
    def producer(self,queue,tup):
        tup=self.tup
        print('Producer: Running')
        # generate items
        self.item = (tup,tup,tup,tup)
        # add to the queue
        queue.put(self.item)
        # report progress
        print(f'>producer added {self.item}')
    # signal that there are no further items

    
    # consumer task
    def consumer(self,queue):
        print('Consumer: Running')
        # consume items
        while True:
            # get a unit of work
            item = queue.get()
            print(item)
            # Veri_Tabani_Window.Ekle(helper.Db_path_time(choice="Now-Day"),0 , 0, 0, 0, 0, 0, 0, 0,str(df.iloc[:]['name'][detect]), Save_image)
            # check for stop
            if item is None:
                break
            # block, to simulate effort
            sleep(item[1])
            # report
            print(f'>consumer got {item}')
        # all done
        print('Consumer: Done')

    def start(self):

        self.queue = Queue()
        print(self.queue)
        consumer = Thread(target=self.consumer, args=(self,self.queue,))
        producer = Thread(target=self.producer, args=(self,self.queue,5))
        consumer.start()
        # start the producer
        producer.start()
        # wait for all threads to finish
        producer.join()
        consumer.join()


        
            
    # # create the shared queue
    # queue = Queue()
    # # start the consumer
    # consumer = Thread(target=consumer, args=(queue,))
    # consumer.start()
    # # start the producer
    # producer = Thread(target=producer, args=(queue,))
    # producer.start()
    # # wait for all threads to finish
    # producer.join()
    # consumer.join()
