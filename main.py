# Gerekli kütüphanelerin immport edilmesi
from compare import *
from db_reader import *
from Cop import *
from ArduinoThread import *
from Arduino_Con import *
from Hata_Goster import *
from PDF_Thread import *
from Pdf_Lister_Thread import *
from post_thread import *
from GirisKayit import *
from Camera import *
from Giris import *
from admin_page import * 
from Camera import*
from Yukleniyor import *
import sys
import time
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    qApp
)

# Yükleniyor ekranı için worker objesinin yaratılması
class Worker(QObject):
    finished = pyqtSignal() # Yükleme işleminin bittiğine dair sinyal
    progress = pyqtSignal(int) # Yükleme işleminin ilerlemesi için gerekli olan sinyal
    

    def run(self): # Worker sınıfının update fonskiyonu 
        
        while 1: 
            time.sleep(0.01)

# Yükleniyor ekranı
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui_ = Ui_LoadingScreen() # Yükleniyor ekranının alınması
        self.setWindowFlag(Qt.FramelessWindowHint) # pencere çubuğunun kaldırılması
        self.ui_.setupUi(self)
        self.show()
        self.execute()

    def execute(self): # Yükleme işleminin başlaması
        self.update_progress(0)
        self.thread = QThread() 
        self.worker = Worker()
        self.worker.moveToThread(self.thread) # Workerın ana thread içinde çalıştırılması

        # sinyallerin fonksiyonlara bağlanması
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.update_progress)

        
        self.thread.start() # threadin başlaması
        main(self.worker, self) # mainin çalıştırılması
        
        
    # Yükleniyor barının güncellenmesi
    def update_progress(self, progress): 
        self.ui_.progressBar.setValue(progress)
        qApp.processEvents()

# worker ve window objesi geçilen main fonksiyonu
def main(worker, window):

    import Db_Con as DC
    from pylonReader import PylonVideoStream
    from Ysa import get_model
    from Helper import Helper
    from ToolKit import ToolKit
    worker.progress.emit(25) # Yükleniyor barının %25 e ayarlanması
    time.sleep(1)
    from os import _exit, mkdir, scandir
    from torch import tensor, device, cuda, cat
    from imutils import resize
    from cv2 import cvtColor, COLOR_BGR2RGB, INTER_CUBIC, imwrite, waitKey, destroyAllWindows
    from cv2 import resize as resize_cv2
    from PyQt5.QtGui import QImage,QPixmap
    from PyQt5.QtCore import QTimer, QTime
    worker.progress.emit(50) # Yükleniyor barının %50 ye ayarlanması
    time.sleep(1)
    from io import BytesIO
    
    from pandas import DataFrame
    from pypylon import pylon
    worker.progress.emit(75) # Yükleniyor barının %75 e ayarlanması
    time.sleep(1)

    # kameraların zoom ayarları için config mapinin oluşturulması
    global configs
    configs =  {
        1: {
            'value1': 0,
            'value3': 0,
            'value5': [0,0]
        },
        2: {
            'value1': 0,
            'value3': 0,
            'value5': [0,0]
        },
        3: {
            'value1': 0,
            'value3': 0,
            'value5': [0,0]
        },
        4: {
            'value1': 0,
            'value3': 0,
            'value5': [0,0]
        },
    }

    # aç butonuna basınca çalışan fonksiyon
    def displayImage():
            MainWindow7.show()
            ui2.logic_All = 1
            ui2.Ac_pushButton.setDisabled(True) # aç butonunun disable yapılması 
            ui2.Off_pushButton.setDisabled(False) # kapat butonunun etkinleştirilmesi
                
    def Soft_Serial_OPEN():
        Tools.Port_Op()
        if Tools.Trigg_Port_Button==True:
            MainWindow7.close()
            Basler_Cameras() # kameraların açılması
            
    def Soft_NSerial_OPEN():
        Tools.Port_Close()
        if Tools.Non_Trigg_Port_Button==True:
            MainWindow7.close()
            Basler_Cameras() # kameraların açılması
            
    def Basler_Cameras():
        try:
            Arduino_Tools.port_ac(Tools)
        except:
            time.sleep(0.1)
            ui2.statusbar.showMessage(" "*1 + " Port açılamadı !!!", 1500)
        
        cnt=0 # hata sayısı sayacı 

        # kameraların saptanması
        tlFactory = pylon.TlFactory.GetInstance()
        devices = tlFactory.EnumerateDevices()
        cameras = pylon.InstantCameraArray(min(len(devices), 2))
        for i, cam in enumerate(cameras):
            cam.Attach(tlFactory.CreateDevice(devices[i]))
            print("Using device ", cam.GetDeviceInfo().GetSerialNumber())

        # kameralar threadi için objenin oluşturulması
        vs_pylon = PylonVideoStream(cameras, Tools).start()

        # fps için gerekli değişkenler
        prev_frame_time = 0
        new_frame_time = 0

        # tensorun oluşturulması
        tensor_temp = tensor([1.0,2.0], device="cuda")
        device_temp = device('cuda' if cuda.is_available() else 'cpu')
        print("CUDA GPU:", cuda.is_available())
        
        if cuda.is_available(): # Cuda aktif ise
            tensor_temp = tensor_temp.to(device_temp)
        myTime = 0
        while 1:
            # dok no ve kalite no nun alınması
            Dok_no= ui3.Dok_No_LineEdit.text()
            Kalite_no= ui3.Kalite_No_LineEdit.text() 
            if not ui3.Kalite_No_LineEdit.text():
                Kalite_no=0
            if not ui3.Dok_No_LineEdit.text():
                Dok_no= 0

            if vs_pylon.cameras.IsCameraDeviceRemoved() : # kamera çıkartılırsa
                # kamerların kapatalıp pixmaplerin ayarlanması
                vs_pylon.cameras.Close()
                pixmap = QPixmap('./Icon/Label Img/CameraOFF.PNG')
                ui2.Camera_1.setPixmap(pixmap) 
                ui2.Camera_2.setPixmap(pixmap) 
                ui2.Camera_3.setPixmap(pixmap) 
                ui2.Camera_4.setPixmap(pixmap) 
                return Basler_Cameras()

            frames = vs_pylon.read() # kameradan gelen framelerin alınması
            
            if ui2.logic_All == 0: # UI logic kapalı durumda ise
                # Kameraları kapat
                vs_pylon.stop() 
                for cam in vs_pylon.Active_cameras:
                    cam.grabResult.Release()
                cameras.StopGrabbing()
                break

            if len(frames) == 0: # hiç kamera bağlı değil ise
                print('No camera is detected!')
                ui2.Off_pushButton.setDisabled(True)
                vs_pylon.stop()
                ui2.Ac_pushButton.setDisabled(False)
                return 

            if len(frames) == 1: # bir kamera var ise
                # görüntü ve kamera serilinin alınması
                model_name = frames[0][1]
                model_image =frames[0][0]
                height, width, channel = model_image.shape

                # zoom değerlerinin alınması
                zoom_value_5 = Tools.zoom_value_5()
                zoom_value_3 = Tools.zoom_value_3()
                zoom_value_1 = Tools.zoom_value_1()


                if ui2.radioButton_Camera_I.isChecked()==True and model_name== Tools.Camera_Serial[0]: # kamera 1 radio butonu seçilitse ve serial numarası doğruysa
                    # zoom işlemi
                    model_image = model_image[zoom_value_5[1]+ zoom_value_3: -zoom_value_5[1]+height  + zoom_value_3, zoom_value_5[0]+zoom_value_1 : width - (zoom_value_5[0])+ zoom_value_1 ]
            

                if ui2.radioButton_Camera_II.isChecked()==True and model_name==Tools.Camera_Serial[1]: # kamera 2 radio butonu seçilitse ve serial numarası doğruysa
                    # zoom işlemi
                    model_image = model_image[zoom_value_5[1]+ zoom_value_3: -zoom_value_5[1]+height  + zoom_value_3, zoom_value_5[0]+zoom_value_1 : width - (zoom_value_5[0])+ zoom_value_1 ]
                
                # fotoğrafın 1400px genişliğe düüşürülmesi    
                single_frame = resize(model_image,  width=1400)
                single_frame2  = resize(model_image, width=1400)
                
                # fps 
                new_frame_time = time.time()
                fps = 1/(new_frame_time-prev_frame_time)
                prev_frame_time = new_frame_time
                fps = int(fps)
                fps = str(fps)
                
                # modele görüntünün sokulması
                results = model(single_frame)         
                results.display(render=True) 

                height, width, channel=results.imgs[0].shape
                step=channel*width

                # görüntü için gerekli alt ve üst sınırların belirlenmesi
                out= cvtColor(results.imgs[0],COLOR_BGR2RGB)
                outh1 = int((64*height)/256)
                outh2 = int((192*height)/256)   
                out[outh1,:] = 0           
                out[outh2,:] = 0

                # model sonrası bulunun hatalarla ilgili dataframe in alınması
                df=results.pandas().xyxy[0]
                df=DataFrame(df)

                myTime+=1
                
                if len(df)!=0: # hata var ise
                    for detect in range(len(df.iloc[:]['name'])): # tüm hataların döndürülmesi
                        # resmi kaydetmek için gerekli pathin oluşturulması
                        Save_image="./Database"+"/"+helper.Db_path_time(choice="Now-Day")+"/"+"Cam"+"/"+"images"+"/"+df.iloc[:]['name'][detect]+"-"+helper.Db_path_time(choice="Now-Time")+"-"+".jpg"
                        
                        # hata koordinatları
                        x1=int(df.iloc[:]['xmin'][detect])
                        x2=int(df.iloc[:]['xmax'][detect])
                        y1=int(df.iloc[:]['ymin'][detect])
                        y2=int(df.iloc[:]['ymax'][detect])
                        classId = df.iloc[:]['class'][detect]
                        cx = (x1 + x2)/ 2
                        cy = (y1 + y2)/ 2
                        
                        # hata sınırlarının güncellenmesi
                        if(x1<=0):x1=0
                        if(y1<=0):y1=0 
                        if (x1<=6):x1=6
                        if(y1<=6):y1=6

                        yc = (y1+y2)/2 # hata merkezi

                        if yc>outh1 and  yc<outh2: # hata belirttiğimiz sınırların içinde kalıyorsa
                            crop=single_frame2[y1-5:y2+5,x1-5:x2+5] # hatanın kırpılması
                                        
                            if Tools.Trigg_Port_Button==True:
                                    Arduino_Tools.kirmizi_led_ac()
                                    try:
                                        src=Arduino_Tools.Feedback_src()
                                    except:
                                        ui2.statusbar.showMessage(" "*1 + "Seri Port Hatası Metre bilgileri 0 Olarak Ayarlandı", 1500)
                                        src=0
                            if Tools.Trigg_Port_Button==False:
                                    src=0

                            # hata uzunluk genişlik ve alanının hesaplanması        
                            x=abs(x2-x1)
                            y=abs(y2-y1)
                            xy=x*y
                            
                            if str(df.iloc[:]['name'][detect])=='Delik' or str(df.iloc[:]['name'][detect])=='Leke': # hata leke veya delık ise
                                cnt=cnt+1 # hata sayısnın artırılması
                            if cnt>=1: 
                                cnt=0
                                if not helper.check_similarity(crop): # hata onceki hatalarla aynı değilse
                                    # hatanın gosterileceği pencerenin açılması
                                    MainWindow6.show() 
                                    crop=resize_cv2(crop, (320,320),interpolation=INTER_CUBIC)
                                    image = QtGui.QImage(crop.data, crop.shape[1], crop.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
                                    ui6.Goster_Label.setPixmap(QtGui.QPixmap.fromImage(image))
                                    ui6.Metre_Label.setText(str(src))
                                    ui6.Sinif_Label.setText(str(df.iloc[:]['name'][detect]))
                                    ui6.Eni_Label.setText(str(x))
                                    ui6.boyu_Label.setText(str(y))
                                    ui6.Alan_Label.setText(str(xy))

                                    # hatanın post request ile veritabanına gönderilmesi
                                    postOut = cvtColor(crop, COLOR_BGR2RGB)
                                    img = Image.fromarray(postOut, "RGB")
                                    img_byte_arr = BytesIO()
                                    img.save(img_byte_arr, format='PNG')
                                    img_byte_arr = img_byte_arr.getvalue()
                                    url= "https://menderes-mobile-app.herokuapp.com/errors/add" # backend urlsi
                                    headers = {'accept': 'application/json',
                                                                    "Authorization":'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MmZiMzVjYjY5YThiZDk5MTUwNjhiYTMiLCJpYXQiOjE2NjA4MzM3NTczNTIsImV4cCI6MTY2MDgzMzg0Mzc1Mn0.tfKjNRPlo7IvDN6Cp2K81Z0wfreNQkJtDsYZAxl4w7T3j4m4fcgVoephYxaUljoGKxli6OsnBvnf7BVoV994Mm_b-nvfp9srm-rqQdCOfsB_GI65GyHwpsnVbLo9uODhcbtcKXWE_x_rBBGphHcU12XXxsHrRTGUkhG5btn7f3JBt9uRrkXiuu_0G9cdFRrha8RwYNs6ZvJo3AuUit1iWGVyWSw7mI92wTBZJWt629ozc1Dd7fMR7j6z_twxLjT9mEKFAd7k4wJUTl4s3upKVZNfTOQP_DBJ9ci_FgpJYwxZqMwQbNF8ltTtyC3TFTZTqczL1dIuFaV44t7eu8FM6OcbklY3dQ-1aYtMMDBWmxUA3zDr7Z50f-ZC5n3YZJlE9hN8d7mcAqN47nbTBzkuofp2kSmhTPWwKce3LJWx9B8ZqWssTSKZegFh_Ldn-xrD8mB7IIDM48D-JgHvLTelIxnGkUDKbg8vL26VR-aJmceL89EYA2K-Kal2FBF18qN7I2icGcMp9k3CDZEeBaTqmVGkqmWGLLKCnxeaN2HVDSdD5bGoPFBVCL6TDgf53HYNRU7WafpL6Ln8MnIdr2n9gm6hKEtTUGam_MrEH54yHKTLi4XcxQbYOV4uavOXA0ICck_WfHbIRo6jLBf-eVmoQP5uHzK4mwhRz3C7NjfZOws'}
                                    data = {
                                                                "class": str(df.iloc[:]['name'][detect]),
                                                                "meterInFabric":  str(src),
                                                                "width": str(x),
                                                                "height": str(y),
                                    }
                                
                                    multiple_files = [
                                            ('photo', ('arda.jpg', img_byte_arr, 'image  /jpg')),
                                            
                                    ]
                                    # post requestin threade gönderilmesi
                                    post_reader.append_post_thread(headers, files=multiple_files, data=data, url=url)

                                    if len(helper.last_images)>=5: # last images dizisinin uzunluğu 5 den büyükse
                                        del helper.last_images[0]  # ilk elemanı sil
                                        helper.last_images.append(crop) # bu hatayı ekle
                                    else: 
                                        helper.last_images.append(crop) # bu hatayı ekle
                                    imwrite(Save_image, single_frame2) # resmin kaydedilmesi
                                    waitKey(1)

                                    # veri tabanına yüklemek için threade gönderilmesi
                                    helper.append_db(df, detect, Save_image, str(src), str(x), str(y), str(xy), Dok_no, Kalite_no)
                                        
                                if Tools.Trigg_Port_Button==True:
                                    Arduino_Tools.kirmizi_led_ac()
                                    try:
                                        src=Arduino_Tools.Feedback_src()
                                    except:
                                        ui2.statusbar.showMessage(" "*1 + "Seri Port Hatası Metre bilgileri 0 Olarak Ayarlandı", 1500)
                                        src=0
        
                            if not str(df.iloc[:]['name'][detect])=='Delik' or not str(df.iloc[:]['name'][detect])=='Leke': #leke veya delik değilse
                                if not helper.check_similarity(crop): # hata onceki hatalarla aynı değilse
                                    if len(helper.last_images)>=5: # last images dizisinin uzunluğu 5 den büyükse
                                        del helper.last_images[0] # ilk elemanı sil
                                        helper.last_images.append(crop) # bu hatayı ekle
                                    else:
                                        helper.last_images.append(crop) # bu hatayı ekle
                                    imwrite(Save_image,crop) # resmin kaydedilmesi

                                    # veri tabanına yüklemek için threade gönderilmesi
                                    helper.append_db(df, detect, Save_image, str(src), str(x), str(y), str(xy), Dok_no, Kalite_no)

                # Serial numarası doğru ise resmin gerekli pixmapa verilmesi
                if model_name == Tools.Camera_Serial[0]:
                    qImg=QImage(out,width,height,step,QImage.Format_RGB888)
                    ui2.Camera_1.setPixmap(QPixmap.fromImage(qImg))
                    
                elif model_name == Tools.Camera_Serial[1]:
                    qImg=QImage(out,width,height,step,QImage.Format_RGB888)
                    ui2.Camera_2.setPixmap(QPixmap.fromImage(qImg))

                elif model_name == Tools.Camera_Serial[2]:
                    qImg=QImage(out,width,height,step,QImage.Format_RGB888)
                    ui2.Camera_2.setPixmap(QPixmap.fromImage(qImg))

                elif model_name == Tools.Camera_Serial[3]:
                    qImg=QImage(out,width,height,step,QImage.Format_RGB888)
                    ui2.Camera_2.setPixmap(QPixmap.fromImage(qImg))
                ui2.label_8.setText(str(fps))
                waitKey(2)
                
            if len(frames) == 2:
                # Kameraların serial ve görüntü alınması
                frame, frame2 = frames[0][0], frames[1][0]
                frame_model, frame2_model = frames[0][1], frames[1][1]
                height, width, channel = frame.shape
                height2, width2, channel2 = frame2.shape
                
                # Zoom
                if ui2.radioButton_Camera_I.isChecked()==True and frame_model == Tools.Camera_Serial[0]:
                    configs[1]['value5'] = Tools.zoom_value_5()
                    configs[1]['value3'] = Tools.zoom_value_3()
                    configs[1]['value1'] = Tools.zoom_value_1()
                if ui2.radioButton_Camera_II.isChecked()==True and frame2_model == Tools.Camera_Serial[1]:
                    configs[2]['value5'] = Tools.zoom_value_5()
                    configs[2]['value3'] = Tools.zoom_value_3()
                    configs[2]['value1'] = Tools.zoom_value_1()
                frame = frame[configs[1]['value5'][1]+ configs[1]['value3']: -configs[1]['value5'][1]+height  + configs[1]['value3'], configs[1]['value5'][0]+configs[1]['value1'] : width - (configs[1]['value5'][0])+ configs[1]['value1']]
                frame2 = frame2[configs[2]['value5'][1]+ configs[2]['value3']: -configs[2]['value5'][1]+height2  + configs[2]['value3'], configs[2]['value5'][0]+configs[2]['value1'] : width2 - (configs[2]['value5'][0])+ configs[2]['value1']]
                # Görüntünün yeniden boyutlandırılması
                frame_1 = resize(frame, width=1400)
                frame_2 = resize(frame2, width=1400)
                
                # Görüntünün cuda ile tensore dönüşümü
                tensor1 = tensor(frame_1, device="cuda")
                tensor2 = tensor(frame_2, device="cuda")

                # Fps ölçümü
                new_frame_time = time.time()
                fps = 1/(new_frame_time-prev_frame_time)
                prev_frame_time = new_frame_time
                fps = int(fps)
                fps = str(fps)
                myTime+=1
                
                # Görüntülerin Birleştirilmesi
                tensor_temp = cat([tensor1, tensor2], dim=0)
                # Tensorlerin CPU'ya atanması
                results = model(tensor.cpu().numpy())
                results.display(render=True)
                h = results.imgs[0].shape[0] 
                out1= cvtColor(results.imgs[0][0:int(h/2), :],COLOR_BGR2RGB)
                out2= cvtColor(results.imgs[0][int(h/2):, :]  ,COLOR_BGR2RGB)
                
                # Kırpma işlemi için kullanılacak görüntünün kopyası
                results_2 = tensor.cpu().numpy()
                
                #
                height, width, channel=out1.shape
                height2, width2, channel2=out2.shape
                step=channel*width
                
                # Benzerlik için y sınırlarının belirlenmesi
                outh1 = int((64*height)/256)
                outh2 = int((192*height)/256)
                outh3 = int((64*height2)/256)
                outh4 = int((192*height2)/256)
                
                # GUIde gözüken görüntünün sınırların çizilmesi
                out1[outh1,:] = 0
                out1[outh2,:] = 0
                out2[outh3,:] = 0
                out2[outh4,:] = 0
                
                #  Görüntü dizisinin oluşturulması
                outs = [[out1, frame_model], [out2, frame2_model]]

                # Hataların koordinatları
                df=results.pandas().xyxy[0]
                df=DataFrame(df)
            
                if len(df)!=0:  # Hata tespit edildiğinde
                    for detect in range(len(df.iloc[:]['name'])):
                        
                        # Resimler için kayıt yolunun belirlenmesi
                        Save_image="./Database"+"/"+helper.Db_path_time(choice="Now-Day")+"/"+"Cam"+"/"+"images"+"/"+df.iloc[:]['name'][detect]+"-"+helper.Db_path_time(choice="Now-Time")+"-"+".jpg"
                        
                        # Hataların koordinatları
                        x1=int(df.iloc[:]['xmin'][detect])
                        x2=int(df.iloc[:]['xmax'][detect])
                        y1=int(df.iloc[:]['ymin'][detect])
                        y2=int(df.iloc[:]['ymax'][detect])
                        
                        # Sınırlardaki hataların önlenmesi
                        if(x1<=0):x1=0
                        if(y1<=0):y1=0 
                        if (x1<=6):x1=6
                        if(y1<=6):y1=6
                        
                        yc = (y1+y2)/2  # Hata koordinatlarının merkezi
                    
                        if (yc>outh1 and  yc<outh2) or (yc>outh3+175 and yc<outh4+175) :  # Hata merkezinin istenilen aralıkta olması
                            crop=results_2[y1-5:y2+5,x1-5:x2+5]   # Hata görüntüsünün kırpılması
                            if Tools.Trigg_Port_Button==True:   # Serial Portun açılması durumunda 
                                    Arduino_Tools.kirmizi_led_ac()
                                    try:
                                        src=Arduino_Tools.Feedback_src()
                                    except:
                                        ui2.statusbar.showMessage(" "*1 + "Seri Port Hatası Metre bilgileri 0 Olarak Ayarlandı", 1500)
                                        src=0
                            if Tools.Trigg_Port_Button==False:
                                    src=0
                            #Hata alanının bulunması
                            x=abs(x2-x1)
                            y=abs(y2-y1)
                            xy=x*y
                            
                            
                            if str(df.iloc[:]['name'][detect])=='Delik' or str(df.iloc[:]['name'][detect])=='Leke': # Hatanın Delik veya Leke olması durumunda
                                cnt=cnt+1
                            if cnt>=1: 
                                cnt=0
                                if not helper.check_similarity(crop):
                                    MainWindow6.show()
                                    crop=resize_cv2(crop, (320,320),interpolation=INTER_CUBIC)
                                    image = QtGui.QImage(crop.data, crop.shape[1], crop.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
                                    ui6.Goster_Label.setPixmap(QtGui.QPixmap.fromImage(image))
                                    ui6.Metre_Label.setText(str(src))
                                    ui6.Sinif_Label.setText(str(df.iloc[:]['name'][detect]))
                                    ui6.Eni_Label.setText(str(x))
                                    ui6.boyu_Label.setText(str(y))
                                    ui6.Alan_Label.setText(str(xy))
                                    
                                    postOut = cvtColor(crop, COLOR_BGR2RGB)
                                    img = Image.fromarray(postOut, "RGB")
                                    img_byte_arr = BytesIO()
                                    img.save(img_byte_arr, format='PNG')
                                    img_byte_arr = img_byte_arr.getvalue()
                                    url= "https://menderes-mobile-app.herokuapp.com/errors/add"
                                    headers = {'accept': 'application/json',
                                                                    "Authorization":'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MmZiMzVjYjY5YThiZDk5MTUwNjhiYTMiLCJpYXQiOjE2NjA4MzM3NTczNTIsImV4cCI6MTY2MDgzMzg0Mzc1Mn0.tfKjNRPlo7IvDN6Cp2K81Z0wfreNQkJtDsYZAxl4w7T3j4m4fcgVoephYxaUljoGKxli6OsnBvnf7BVoV994Mm_b-nvfp9srm-rqQdCOfsB_GI65GyHwpsnVbLo9uODhcbtcKXWE_x_rBBGphHcU12XXxsHrRTGUkhG5btn7f3JBt9uRrkXiuu_0G9cdFRrha8RwYNs6ZvJo3AuUit1iWGVyWSw7mI92wTBZJWt629ozc1Dd7fMR7j6z_twxLjT9mEKFAd7k4wJUTl4s3upKVZNfTOQP_DBJ9ci_FgpJYwxZqMwQbNF8ltTtyC3TFTZTqczL1dIuFaV44t7eu8FM6OcbklY3dQ-1aYtMMDBWmxUA3zDr7Z50f-ZC5n3YZJlE9hN8d7mcAqN47nbTBzkuofp2kSmhTPWwKce3LJWx9B8ZqWssTSKZegFh_Ldn-xrD8mB7IIDM48D-JgHvLTelIxnGkUDKbg8vL26VR-aJmceL89EYA2K-Kal2FBF18qN7I2icGcMp9k3CDZEeBaTqmVGkqmWGLLKCnxeaN2HVDSdD5bGoPFBVCL6TDgf53HYNRU7WafpL6Ln8MnIdr2n9gm6hKEtTUGam_MrEH54yHKTLi4XcxQbYOV4uavOXA0ICck_WfHbIRo6jLBf-eVmoQP5uHzK4mwhRz3C7NjfZOws'}
                                    data = {
                                                                "class": str(df.iloc[:]['name'][detect]),
                                                                "meterInFabric":  str(src),
                                                                "width": str(x),
                                                                "height": str(y),
                                    }
                                
                                    multiple_files = [
                                            ('photo', ('arda.jpg', img_byte_arr, 'image  /jpg')),
                                            
                                    ]
        
                                    post_reader.append_post_thread(headers, files=multiple_files, data=data, url=url)
                                    if len(helper.last_images)>=5:
                                        del helper.last_images[0]
                                        helper.last_images.append(crop)
                                    else:
                                        helper.last_images.append(crop)
                                    imwrite(Save_image, results_2)
                                    helper.append_db(df, detect, Save_image, str(src), str(x), str(y), str(xy), Dok_no, Kalite_no)
                                        
                                if Tools.Trigg_Port_Button==True:
                                    Arduino_Tools.kirmizi_led_ac()
                                    try:
                                        src=Arduino_Tools.Feedback_src()
                                    except:
                                        ui2.statusbar.showMessage(" "*1 + "Seri Port Hatası Metre bilgileri 0 Olarak Ayarlandı", 1500)
                                        src=0
        
                            if not str(df.iloc[:]['name'][detect])=='Delik' or not str(df.iloc[:]['name'][detect])=='Leke':
                                if not helper.check_similarity(crop):
                                    if len(helper.last_images)>=5:
                                        del helper.last_images[0]
                                        helper.last_images.append(crop)
                                    else:
                                        helper.last_images.append(crop)
                                    imwrite(Save_image,crop)
                                    helper.append_db(df, detect, Save_image, str(src), str(x), str(y), str(xy), Dok_no, Kalite_no)
        
                for out in outs:
                    
                    if out[1] == Tools.Camera_Serial[0]:
                        out_1= cvtColor(out[0],COLOR_BGR2RGB)
                        qImg=QImage(out_1,width,height,step,QImage.Format_RGB888)
                        ui2.Camera_1.setPixmap(QPixmap.fromImage(qImg))
                    if out[1] == Tools.Camera_Serial[1]:
                        qImg=QImage(out[0],width,height,step,QImage.Format_RGB888)
                        ui2.Camera_2.setPixmap(QPixmap.fromImage(qImg))
                    if out[1] == Tools.Camera_Serial[2]:
                        qImg=QImage(out[0],width,height,step,QImage.Format_RGB888)
                        ui2.Camera_3.setPixmap(QPixmap.fromImage(qImg))
                    if out[1] == Tools.Camera_Serial[3]:
                        qImg=QImage(out[0],width,height,step,QImage.Format_RGB888)
                        ui2.Camera_4.setPixmap(QPixmap.fromImage(qImg))
                waitKey(2)
                ui2.label_8.setText(str(fps))
                            
        destroyAllWindows()     


    def Video_Selected():
        ui2.Durum_Cam.setText("AÇIK")
        if ui2.Camera_comboBox.currentText()=="I. Kamera":
            ui2.Cam_I_Record=1
            print("Video Start I")
        elif ui2.Camera_comboBox.currentText()=="II. Kamera":
            ui2.Cam_II_Record=1
            print("Video Start II")
            
        elif ui2.Camera_comboBox.currentText()=="III. Kamera":
            ui2.Cam_III_Record=1
            print("Video Start III")
            
        elif ui2.Camera_comboBox.currentText()=="IV. Kamera":
            ui2.Cam_IV_Record=1
            print("Video Start IV")
            
    ########################################################################################################################
    ##Kayıt etmenin durdurulması
    def Click_Button_Stop():
        ui2.Cam_I_Record=0
        ui2.Cam_II_Record=0
        ui2.Cam_III_Record=0
        ui2.Cam_IV_Record=0
        ui2.Durum_Cam.setText("KAPALI")
    ##Bütün Kameraların Kapatılması Buttonu
    def Click_Button_All_Stop():
        Arduino_Tools.hepsini_kapat()
        Arduino_Tools.port_kapat()
        ui2.logic_All=0
        ui2.Ac_pushButton.setDisabled(False)
        ui2.Off_pushButton.setDisabled(True)
        pixmap = QPixmap('./Icon/Label Img/CameraOFF.PNG')
        ui2.Camera_1.setPixmap(pixmap) 
        ui2.Camera_2.setPixmap(pixmap) 
        ui2.Camera_3.setPixmap(pixmap) 
        ui2.Camera_4.setPixmap(pixmap) 
        Tools.Non_Trigg_Port_Button=False
        Tools.Trigg_Port_Button=False
        

        ui2.label_9.setText(str(0))
    ## Çıkış Buttonu

    ########################################################################################################################
    def Close():
        MainWindow1.close()
        MainWindow2.close()
        MainWindow3.close()
        MainWindow4.close()
        MainWindow5.close()

        destroyAllWindows()
        ui2.logic_All=0
        app1.quit()
        app2.quit()
        app3.quit()
        app4.quit()
        app5.quit()
        _exit(0)
        
    ########################################################################################################################
    #SAAT
    def showTime():
        # Şimdiki zaman Current Time
        current_time = QTime.currentTime()
        # String Dönüşümü
        label_time = current_time.toString('hh:mm:ss')
        # Label üzerinde gösterim
        ui2.label_11.setText(label_time)

    ########################################################################################################################
    def UiComponents():
        Start()
        timer = QTimer()
        Show_Record_Time()
        timer.timeout.connect(Show_Record_Time)
        timer.start(10)
    def Show_Record_Time():
        if ui2.flag:
            ui2.count+= 1
        ui2.text = str(ui2.count / 20)
        ui2.label_9.setText(ui2.text)
    def Start():
        ui2.flag = True
    def Re_set():
        ui2.flag = False
        ui2.count = 0
        ui2.label_9.setText(str(ui2.count))    
        
    ########################################################################################################################
    #Gün bazlı klasör oluşturma
    def New_Day_Create_Folder(name):
        day_db_is_here = helper.readVideo()[0]
        mkdir(day_db_is_here+"/"+name)
        
    def New_Day_Folder():
        day_db_is_here = helper.readVideo()[0]
        day=helper.now.day
        month=helper.now.month
        year=helper.now.year
        now=str(day)+"."+str(month)+"."+str(year)
        obj=scandir(day_db_is_here)
        for entry in obj:
            if entry.is_dir() or entry.is_file():
                if entry.name==now:
                    print("Klasör Oluşturulmuş")
                else:
                    try:
                        New_Day_Create_Folder(now)
                        print(day_db_is_here)
                        mkdir(day_db_is_here+"/"+now+"/"+"Cam")
                        mkdir(day_db_is_here+"/"+now+"/"+"Cam"+"/"+"images")
                        mkdir(day_db_is_here+"/"+now+"/"+"Cam"+"/"+"videos")
                        break
                    except:
                        print("Klasör Zaten var")
                        break
                    
    ########################################################################################################################
    def starting_upload():
        Tools.default_upload()
        configs[1] = Tools.feedback_js()['1']
        configs[2] = Tools.feedback_js()['2']
        configs[3] = Tools.feedback_js()['3']
        configs[4] = Tools.feedback_js()['4']

    def default_model():
        path = Veri_Tabani_Window.get_last_model_path()
        Tools.Model_Path = path
        
    def Upload_Cameras_Inf():
        _Camera_Height, _Camera_Width, _Camera_Impact_Rate, _Camera_Serial, _Camera_Exposure_Time, _Camera_Cut_Off, _Cameras_Type= Tools.feedback_Splited_Last_Data()
        Veri_Tabani_Window.Last_Cameras_Info_Add(_Camera_Height, _Camera_Width, _Camera_Impact_Rate, _Camera_Serial, _Camera_Exposure_Time, _Camera_Cut_Off, _Cameras_Type,
        )
        
    def handle_upload():

        valid = Tools.upload()
        if valid:
            configs[1] = Tools.feedback_js()['1']
            configs[2] = Tools.feedback_js()['2']
            configs[3] = Tools.feedback_js()['3']
            configs[4] = Tools.feedback_js()['4']

            if ui2.radioButton_Camera_I.isChecked():
                Tools.handle_change(configs[1])
            if ui2.radioButton_Camera_II.isChecked():
                Tools.handle_change(configs[2])
    def Pdf_Show():
        PDFThread().start()
        PDFThread().stop()
        
    def Pdf_Lister():
        Date=DC.ui3.Baslangic_dateEdit.text().split('.')
        DateLast=DC.ui3.Bitis_dateEdit.text().split('.')
        PDFThread_Lister(Date, DateLast).start()

    def Camera_Inf():
        Tools.Import_Height()
        Tools.Import_Width()
        Tools.Import_Camera_Serial()
        Tools.Import_Camera_Exposure_Time()
        Tools.Import_Cameras_Type()
    
    print("Arayüzlerin Yüklenmesi")
    Arduino_Tools=Arduino_Toolkits()
    print("Arduino Toolkit Yüklendi")
    Tools=ToolKit()
    print("Toolkit Yüklendi")
    helper = Helper().start()
    print("Helper Yüklendi")
    post_reader = post_thread()
    print("Mobil araçları Yüklendi")
    post_reader.post_thread_start()
    model = get_model(Tools)
    print("Yapay Zeka Yüklendi")

    ################################################ Giris ################################################
    MainWindow1,MainWindow2,MainWindow3,MainWindow4,MainWindow5=Tools.FeedBack_Windows()
    ui1,ui2,ui3,ui4,ui5=Tools.FeedBack_SetupUi()
    app1,app2,app3,app4,app5=Tools.FeedBack_App()
    zoom_impact_rate=Tools.FeedBack_Zoom_Rate()
    app6,MainWindow6,ui6=Arduino_Tools.FeedBack_MainWindow_Error()
    ui7, MainWindow7, app7 = Tools.FeedBack_Port_UI()
    ui8, MainWindow8, app8 = Tools.Feedback_Kayt_UI()
    #######################################################################################################

    worker.progress.emit(100)
    time.sleep(0.5)
    window.close()
    worker.finished.emit()
    
    MainWindow1.show()
    Tools.Cam_out_file_folder()
    New_Day_Folder()
    Veri_Tabani_Window.Listele()
    Veri_Tabani_Window.get_last_path()
    Veri_Tabani_Window.get_last_Heigt_Width()
    ui2.logic_All = 0
    ui2.Off_pushButton.setDisabled(True)
    pixmap = QPixmap('./Icon/Label Img/CameraOFF.PNG')
    ui2.Camera_1.setPixmap(pixmap) 
    ui2.Camera_2.setPixmap(pixmap) 
    ui2.Camera_3.setPixmap(pixmap) 
    ui2.Camera_4.setPixmap(pixmap) 
    starting_upload()
    default_model()
    timer = QTimer()
    timer.timeout.connect(showTime)
    timer.start(1000)
    
    ##Slotlar
    #######################
    get_log_reg=GirisVKayit(app1, ui1, ui2, ui8, MainWindow1, MainWindow2, MainWindow8, Veri_Tabani_Window.get_users_inf(), Veri_Tabani_Window)
    ui1.Giris_pushButton.clicked.connect(lambda : get_log_reg.Giris("Camera"))
    ui1.Kayit_pushButton.clicked.connect(lambda : get_log_reg.Giris("Kayit"))
    ui2.Start_pushButton.clicked.connect(Video_Selected)
    ui2.Stop_pushButton.clicked.connect(Click_Button_Stop)
    ui2.Off_pushButton.clicked.connect(Click_Button_All_Stop)
    ui2.Close_pushButton.clicked.connect(Close)
    ui2.Ac_pushButton.clicked.connect(displayImage)
    ui2.horizontalSlider.valueChanged.connect(Tools.zoom_value_1)
    ui2.horizontalSlider_3.valueChanged.connect(Tools.zoom_value_3)
    ui2.horizontalSlider_5.valueChanged.connect(Tools.zoom_value_5)
    ui2.radioButton_Camera_I.clicked.connect(lambda: Tools.handle_change(configs[1]))
    ui2.radioButton_Camera_II.clicked.connect(lambda: Tools.handle_change(configs[2]))
    ui2.Gezginler.clicked.connect(lambda: Tools.download(configs, helper.now.strftime('%H.%M.%S')))
    ui2.Gezginler_2.clicked.connect(handle_upload)
    ui2.actionVeri_Taban_Penceresi.triggered.connect(Tools.QWindow_DataBase)
    ui2.actionAdmin_Paneli.triggered.connect(Tools.QWindow_Admin)
    ui2.action_k.triggered.connect(Close)
    DC.ui3.actionKameralar.triggered.connect(Tools.QWindow_Camera)
    DC.ui3.actionAdmin_Paneli.triggered.connect(Tools.QWindow_Admin)
    DC.ui3.Temiz_pushButton.clicked.connect(Veri_Tabani_Window.Clear)
    DC.ui3.Veri_Tabani_Widget.itemSelectionChanged.connect(Veri_Tabani_Window.Doldur)
    DC.ui3.Goster_pushButton.clicked.connect(Veri_Tabani_Window.Ara)
    DC.ui3.Raporla_PushButton.clicked.connect(Pdf_Show)
    DC.ui3.Listele_pushButton.clicked.connect(Pdf_Lister)
    DC.ui3.Gunclle_PushButton.clicked.connect(Veri_Tabani_Window.Update)
    DC.ui3.Delete_PushButton.clicked.connect(Veri_Tabani_Window.Delete)
    # DC.ui4.Off_pushButton.clicked.connect(lambda: DC.MainWindow4.close())
    ui5.pushButton_Find_File.clicked.connect(Tools.getFile)
    ui5.pushButton_Aktar_Ysa.clicked.connect(Tools.Import_Model)
    ui5.pushButton_Aktar_Kamera.clicked.connect(Camera_Inf)
    ui5.pushButton_Aktar_Serial_Port.clicked.connect(Tools.Import_Serial_Port)
    ui5.pushButton_Upload.clicked.connect(Upload_Cameras_Inf)
    ui5.actionKameralar.triggered.connect(Tools.QWindow_Camera)
    ui5.actionVeri_Taban.triggered.connect(Tools.QWindow_DataBase)
    ui6.Ikaz_kapat_pushButton.clicked.connect(Arduino_Tools.hepsini_kapat)
    ui7.Ac_pushButton.clicked.connect(Soft_Serial_OPEN)
    ui7.Kapat_pushButton.clicked.connect(Soft_NSerial_OPEN)
    ui8.Giris_pushButton.clicked.connect(lambda : get_log_reg.kayit())


if __name__ == '__main__':
    app1 = QApplication(sys.argv)
    window = MainWindow()
    app1.exec_()
    