from threading import Thread, Timer
import json
import requests
import time

class post_thread():
    def __init__(self):
       self.post_queue=[]
       print("__init__: " + str(self.post_queue))
       self.stopped = False

    def post_thread_start(self):
        Thread(target=self.update_post_thread, args=()).start()
        return self
    
    def update_post_thread(self):
        while True:
            time.sleep(0.0001)
            if self.post_queue:
                task=self.post_queue.pop(0)
                response = requests.post(task['url'], headers=task['headers'], data=task['data'], files=task['files'])
                print("Status Code", response.status_code)
                print("JSON Response ", response.json())
                self.post_queue.clear()
            else:
                continue

    def append_post_thread(self, headers, files, data, url):
        task ={
            "headers": headers,
            "files": files,
            "data": data,
            "url": url
              }
        self.post_queue.append(task)