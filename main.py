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
from whitedetect import *
from image_dimension_converter import *
from threshold import *
from mail_send import *
import time
import sys
import psutil
import logging
import traceback
import datetime


from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    qApp
)

# Log ayarları
logging.basicConfig(filename='app_logs.txt')

logging.info("Program başlatıldı.")


class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    def run(self):
        while 1:
            time.sleep(0.01)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui_ = Ui_LoadingScreen()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.ui_.setupUi(self)
        icon_loading = QPixmap("./Icon/MainWindow/Loadign-Logo.png")
        self.ui_.Logo.setPixmap(icon_loading)
        self.show()
        self.execute()
        
    def execute(self):
        self.update_progress(0)
        self.thread = QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.update_progress)
        self.thread.start()
        main(self.worker, self)
        
    def update_progress(self, progress):
        self.ui_.progressBar.setValue(progress)
        qApp.processEvents()
        
    

def main(worker, window):
    def loadingbar(x):
        worker.progress.emit(x)
        sleep(1./120)
    loadingbar(5)
    import Db_Con as DC
    loadingbar(10)
    from pylonReader import PylonVideoStream
    loadingbar(15)
    from Ysa import get_model
    loadingbar(20)
    from Helper import Helper
    loadingbar(25)
    from ToolKit import ToolKit
    loadingbar(30)
    from os import _exit, mkdir, scandir
    loadingbar(35)
    from torch import tensor, device, cuda, cat
    loadingbar(40)
    from imutils import resize
    loadingbar(45)
    from cv2 import cvtColor, COLOR_BGR2RGB, INTER_CUBIC, imwrite, waitKey, destroyAllWindows, imshow
    loadingbar(50)
    from cv2 import resize as resize_cv2
    loadingbar(55)
    from PyQt5.QtGui import QImage,QPixmap
    loadingbar(60)
    from PyQt5.QtCore import QTimer, QTime
    loadingbar(65)
    from io import BytesIO
    loadingbar(70)
    from pandas import DataFrame
    loadingbar(75)
    from pypylon import pylon
    loadingbar(80)
    import random
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
    
    def displayImage():
            Tools.Port_Op()
            quality = ui2.comboBox_Kalite_No.currentText()
            dok_num = ui2.lineEdit_Dok_No.text()
            if not quality or quality == "Kalite seçiniz":
                ui10.warning_label.setText("Kalite Kodunu giriniz Lütfen. Kapatmak için butona tıklayınız lütfen...")
                Tools.QWarning_Window()
            elif not dok_num:
                Tools.QWarning_Window()
            else:
                # MainWindow7.show()
                ui2.logic_All = 1
                MainWindow9.showMaximized()
                ui2.Ac_pushButton.setDisabled(True)
                ui2.Kayit_pushButton_2.setDisabled(True)
                ui2.Off_pushButton.setDisabled(False)
                Basler_Cameras()
                
    def Soft_Serial_OPEN():
        Tools.Port_Op()
        MainWindow7.close()
        MainWindow9.showMaximized()
        Basler_Cameras()
        # if Tools.Trigg_Port_Button==True:
        #     MainWindow7.close()
        #     MainWindow9.showMaximized()
        #     Basler_Cameras()
            
    def Soft_NSerial_OPEN():
        Tools.Port_Close()
        if Tools.Non_Trigg_Port_Button==True:
            MainWindow7.close()
            MainWindow9.showMaximized()
            Basler_Cameras()

    def record_cameras_data():
        ui2.logic_All = 1
        ui2.Ac_pushButton.setDisabled(True)
        ui2.Off_pushButton.setDisabled(False)
        Tools.Port_Close()
        if Tools.Non_Trigg_Port_Button==True:
            MainWindow7.close()
            Basler_Cameras(choise = "Record")

    def Basler_Cameras(choise: str = "Detection"):
        New_Day_Folder()
        selected_item = ui2.comboBox_Kalite_No.currentText()
        try:
            Arduino_Tools.port_ac(Veri_Tabani_Window())
            brightnessValue = Veri_Tabani_Window().get_fabric_brightness(selected_item)
            sleep(1./5)
            Arduino_Tools.setBrightness(str(brightnessValue))
            sleep(1./5)
            Arduino_Tools.setBrightness(str(brightnessValue))
        except Exception as e:
            logging.error(f'Hata meydana geldi: {str(e)}')
            logging.error(f'Hatanın meydana geldiği kod satırı: {traceback.format_exc()}')

            brightnessValue = Veri_Tabani_Window().get_fabric_brightness(selected_item)
            time.sleep(0.1)
            ui2.statusbar.showMessage(" "*1 + " Port açılamadı !!!", 1500)
        faulty_cnt = 0
        faulty_cnt_100 = 0
        theta_1_center, theta_2_center = [0, 0]
        detect_threshold = 3
        detect_threshold_100 = 10
        detect_cam = 0
        threshold = 200
        wDetect = False
        start_time_faulty_cnt = 0
        start_time_faulty_cnt_100 = 0
        limited_time_faulty = 6
        limited_time_faulty_100 = 120
        detect_faulty_fabric = {"Flawed Hole": 0, "Flawed Spot": 0, "Flawed Crack": 0, "Other Errors": 0}
        start_time_crack_cnt = 0
        limited_time_crack = 18
        crack_ready = False
        
        myTime = 0
        recordcounter = 0
        prev_time = time.time()
        position = 0
        speed = 0
        prev_frame_time = 0
        new_frame_time = 0
        ########################################################################################################################
        #Pixel to mm
        local_height, vision_weight, vision_height, vision_angle = Veri_Tabani_Window().get_Camera_Local_Settings()
        # print(vision_weight)
        resolution_pixels_height, resolution_pixels_width, _ = Veri_Tabani_Window().get_last_Heigt_Width()
        # print(resolution_pixels_width)
        width_converter = WidthConverter(vision_weight, resolution_pixels_width)
        ########################################################################################################################
        tlFactory = pylon.TlFactory.GetInstance()
        devices = tlFactory.EnumerateDevices()
        cameras = pylon.InstantCameraArray(min(len(devices), 3))
        device_indices = []
        for serial in Tools.Camera_Serial:
            for i, devic in enumerate(devices):
                if devic.GetSerialNumber() == serial:
                    device_indices.append(i)
                    break
            else:
                device_indices.append(None)
        for i, cam in enumerate(cameras):
            # print(cam.GetDeviceInfo().GetSerialNumber())
            device_index = device_indices[i]
            if device_index is not None:
                cam.Attach(tlFactory.CreateDevice(devices[device_index]))
                serial_cam = cam.GetDeviceInfo().GetSerialNumber()
                print("Using device ", serial_cam)
                ui2.statusbar.showMessage(" "*1 + f" Tanımlı kamera: {serial_cam}", 1500)
        vs_pylon = PylonVideoStream(cameras, Tools).start()
        tensor_temp = tensor([1.0,2.0], device="cuda")
        device_temp = device('cuda' if cuda.is_available() else 'cpu')
        ui2.statusbar.showMessage( " " * 1 + f" Cuda GPU Durumu: {cuda  .is_available()}", 1500)
        if cuda.is_available():
            tensor_temp = tensor_temp.to(device_temp)
        class_thresholds, error_thresholds, type_speed = Veri_Tabani_Window().get_fabric_settings(selected_item)
        while 1:
            current_time_target = datetime.datetime.now()
            if current_time_target.hour == 0 and 0 < current_time_target.minute < 2:
               New_Day_Folder()
            position, speed = Arduino_Tools.Feedback_src()
            position: int = int(position) / 1000
            speed: int = int(speed)
            if speed > 120:
                ui9.text_Dok_Hizi.setText("0")
            else:
                ui9.text_Dok_Hizi.setText(str(speed))
                
            if position is None:
                ui9.text_Metre_Durumu.setText(str(int(0)))
            else:
                ui9.text_Metre_Durumu.setText(str(int(position)))
            Dok_no= ui2.lineEdit_Dok_No.text()
            Kalite_no= ui2.comboBox_Kalite_No.currentText()
            if vs_pylon.cameras.IsCameraDeviceRemoved() :
                vs_pylon.cameras.Close()
                pixmap = QPixmap('./Icon/Label Img/CameraOFF.PNG')
                ui2.Camera_1.setPixmap(pixmap) 
                ui2.Camera_2.setPixmap(pixmap) 
                ui2.Camera_3.setPixmap(pixmap) 
                ui2.Camera_4.setPixmap(pixmap) 
                return Basler_Cameras()
            try:
                frames = vs_pylon.read()
            except Exception as e:
                logging.error(f'Hata meydana geldi: {str(e)}')
                logging.error(f'Hatanın meydana geldiği kod satırı: {traceback.format_exc()}')
                return
            if ui2.logic_All == 0:
                vs_pylon.stop()
                for cam in vs_pylon.Active_cameras:
                    cam.grabResult.Release()
                cameras.StopGrabbing()
                break

            if len(frames) == 0:
                print('No camera is detected!')
                ui2.statusbar.showMessage(" "*1 + " Tanımlı kamera bulunmamaktadır. Lütfen kamera takılı ise admin panelinden ayarlayınız...", 1500)
                ui2.Off_pushButton.setDisabled(True)
                vs_pylon.stop()
                ui2.Ac_pushButton.setDisabled(False)
                return 

            if len(frames) == 1:
                Dok_no= ui2.lineEdit_Dok_No.text()
                Kalite_no= ui2.comboBox_Kalite_No.currentText()
                model_name = frames[0][1]
                model_image = frames[0][0]
                model_image = model_image[:-1, :-1, :] 
                model_image, cloth_width = ImageProcessor(image=model_image, trim_size=75).trim_image()
                try:
                    cloth_width = int(round(width_converter.convert(cloth_width) / 10, 2))
                except Exception as e:
                    logging.error(f'Hata meydana geldi: {str(e)}')
                    logging.error(f'Hatanın meydana geldiği kod satırı: {traceback.format_exc()}')
                    cloth_width=0
                copy_model_image = np.copy(model_image)
                height, width, channel = model_image.shape
                zoom_value_5 = Tools.zoom_value_5()
                zoom_value_3 = Tools.zoom_value_3()
                zoom_value_1 = Tools.zoom_value_1()
                if ui2.radioButton_Camera_I.isChecked()==True and model_name== Tools.Camera_Serial[0]:
                    model_image = model_image[zoom_value_5[1]+ zoom_value_3: -zoom_value_5[1]+height  + zoom_value_3, zoom_value_5[0]+zoom_value_1 : width - (zoom_value_5[0])+ zoom_value_1 ]
                if ui2.radioButton_Camera_II.isChecked()==True and model_name==Tools.Camera_Serial[1]:
                    model_image = model_image[zoom_value_5[1]+ zoom_value_3: -zoom_value_5[1]+height  + zoom_value_3, zoom_value_5[0]+zoom_value_1 : width - (zoom_value_5[0])+ zoom_value_1 ]
                new_frame_time = time.time()
                fps = 1/(new_frame_time-prev_frame_time)
                prev_frame_time = new_frame_time
                fps = str(int(fps))
                results = model(model_image, size=2048)         
                results.render()
                out = cvtColor(results.ims[0], COLOR_BGR2RGB)
                outh1 = int((43*height)/256)
                outh2 = int((213*height)/256)
                out[outh1,:] = 0           
                out[outh2,:] = 0
                df=results.pandas().xyxy[0]
                df=DataFrame(df)
                myTime+=1
                def y_detect(cy, theta_1_center, theta_2_center, cx):
                    if 0 <= cy <= model_image.shape[0] * 1:
                        detect_cam = 1
                        cv2.line(out, (int(theta_1_center), (detect_cam-1) * height), (int(theta_1_center), height*detect_cam), (0, 255, 0), thickness=2)
                        cv2.line(out, (int(theta_2_center), (detect_cam-1) * height), (int(theta_2_center), height*detect_cam), (0, 255, 0), thickness=2)
                        faulty_meter = round(width_converter.convert(cx) / 10, 2)
                        return detect_cam, out, faulty_meter
                    elif model_image.shape[0] * 1 < cy <= model_image.shape[0] * 2:
                        detect_cam = 2
                        cv2.line(out, (int(theta_1_center), (detect_cam-1) * height), (int(theta_1_center), height*detect_cam), (0, 255, 0), thickness=2)
                        cv2.line(out, (int(theta_2_center), (detect_cam-1) * height), (int(theta_2_center), height*detect_cam), (0, 255, 0), thickness=2)      
                        faulty_meter = round(width_converter.convert(cx + width) / 10, 2) 
                        return detect_cam, out, faulty_meter
                    elif model_image.shape[0] * 2 < cy <= model_image.shape[0] * 3:
                        detect_cam = 3
                        cv2.line(out, (int(theta_1_center), (detect_cam-1) * height), (int(theta_1_center), height*detect_cam), (0, 255, 0), thickness=2)
                        cv2.line(out, (int(theta_2_center), (detect_cam-1) * height), (int(theta_2_center), height*detect_cam), (0, 255, 0), thickness=2)      
                        faulty_meter = round(width_converter.convert(cx + width * 2) / 10, 2)
                        return detect_cam, out, faulty_meter
                    return detect_cam
                single_frame = resize(out,  width=1400)
                height_s, width_s, channel_s = single_frame.shape
                step_s = channel_s * width_s 
                if len(df)!=0:
                    for detect in range(len(df.iloc[:]['name'])):
                        Save_image="./Database"+"/"+helper.Db_path_time(choice="Now-Day")+"/"+"Cam"+"/"+"images"+"/"+df.iloc[:]['name'][detect]+"-"+helper.Db_path_time(choice="Now-Time")+"-"+".jpg"
                        Save_crop_image = "./Database"+"/"+helper.Db_path_time(choice="Now-Day")+"/"+"Cam"+"/"+"images"+"/"+"cropped"+"/"+df.iloc[:]['name'][detect]+"-"+helper.Db_path_time(choice="Now-Time")+"-"+".jpg"

                        x1=int(df.iloc[:]['xmin'][detect])
                        x2=int(df.iloc[:]['xmax'][detect])
                        y1=int(df.iloc[:]['ymin'][detect])
                        y2=int(df.iloc[:]['ymax'][detect])
                        cx = (x1 + x2)/ 2
                        cy = (y1 + y2)/ 2
                        if(x1<=0):x1=0
                        if(y1<=0):y1=0 
                        if (x1<=56):x1=56
                        if(y1<=56):y1=56
                        yc = (y1+y2)/2
                        if yc>outh1 and yc<outh2:
                            new_x1, new_x2, new_y1, new_y2 = Tools.expand(copy_model_image.shape, x1, x2, y1, y2, [10.5, 5.5, 1.1])
                            try:
                                crop = copy_model_image[new_y1:new_y2,new_x1:new_x2]
                            except Exception as e:
                                logging.error(f'Hata meydana geldi: {str(e)}')
                                logging.error(f'Hatanın meydana geldiği kod satırı: {traceback.format_exc()}')
                                crop = copy_model_image[y1:y2,x1:x2]
                            if Tools.Trigg_Port_Button == True:
                                try:
                                    src, speed = Arduino_Tools.Feedback_src()
                                    src: int = int(int(src) / 1000)
                                    speed: int = int(speed)
                                except Exception as e:
                                    logging.error(f'Hata meydana geldi: {str(e)}')
                                    logging.error(f'Hatanın meydana geldiği kod satırı: {traceback.format_exc()}')
                                    ui2.statusbar.showMessage(" "*1 + "Seri Port Hatası Metre bilgileri 0 Olarak Ayarlandı", 1500)
                                    src=0
                            if Tools.Trigg_Port_Button==False:
                                src=0
                            
                            x = abs(x2-x1)
                            y = abs(y2-y1)
                            x = round(width_converter.convert(x), 2)
                            y = round(width_converter.convert(y), 2)
                            xy = round(x * y, 2)
                            if (str(df.at[detect, 'name']) in ['dikis']):
                                start_time_crack_cnt = time.time()
                                crack_ready = False

                            if (str(df.at[detect, 'name']) in ['delik', 'leke', 'kirik']):
                                if faulty_cnt == 0:
                                    start_time_faulty_cnt = time.time()
                                    theta_1_center = max(0, cx - threshold)
                                    theta_2_center = min(model_image.shape[1], cx + threshold)
                                    y_detect_1, single_frame, faulty_meter = y_detect(cy, theta_1_center, theta_2_center, cx)
                                    print(f"yakalanan kamera: {y_detect_1}")
                                y_detect_2, single_frame, faulty_meter = y_detect(cy, theta_1_center, theta_2_center, cx)
                                if faulty_cnt_100 == 0:
                                    start_time_faulty_cnt_100 = time.time()
                                try:
                                    crop = resize_cv2(crop, (320,320), interpolation = INTER_CUBIC)
                                except Exception as e:
                                    logging.error(f'Hata meydana geldi: {str(e)}')
                                    logging.error(f'Hatanın meydana geldiği kod satırı: {traceback.format_exc()}')
                                    crop = np.zeros((320, 320), dtype=np.uint8)
                                faulty_meter = int(round(width_converter.convert(cx) / 10, 2) )
                                image2 = QtGui.QImage(crop.data, crop.shape[1], crop.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
                                image3 = QtGui.QImage(single_frame.data, single_frame.shape[1], single_frame.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
                                ui6.Goster_Label.setPixmap(QtGui.QPixmap.fromImage(image2))
                                detect_images.insert(0, image2)
                                show_images.insert(0, single_frame)
                                detect_Faulty_Windows.insert(0, image3)
                                detect_Hata_Eni.insert(0, str(x))
                                detect_Hata_Boyu.insert(0, str(y))
                                detect_Hata_Alan.insert(0, str(faulty_meter))
                                detect_Hata_Metre.insert(0, str(src))
                                detect_Hata_Sinif.insert(0, str(df.iloc[:]['name'][detect]))

                                # detect_images için değişiklik
                                if len(detect_images) > max_data_count:
                                    del detect_images[max_data_count:]
                                for index in range(len(detect_images)):
                                    index2 = index % 6
                                    index3 = page_num[index2]
                                    try:
                                        if str(df.at[detect, 'name']) in error_thresholds:
                                            Hata_Goster_labels[index2].setPixmap(QtGui.QPixmap.fromImage(detect_images[index3]))
                                            Hata_Eni_labels[index2].setText(detect_Hata_Eni[index3])
                                            Hata_Boyu_labels[index2].setText(detect_Hata_Boyu[index3])
                                            Hata_Alan_labels[index2].setText(detect_Hata_Alan[index3])
                                            Hata_Metre_Labels[index2].setText(detect_Hata_Metre[index3])
                                            Hata_Sinif_labels[index2].setText(detect_Hata_Sinif[index3])
                                    except Exception as e:
                                        logging.error(f'Hata meydana geldi: {str(e)}')
                                        logging.error(f'Hatanın meydana geldiği kod satırı: {traceback.format_exc()}')
                                        pass
                                # detect_Faulty_Windows için değişiklik
                                if len(detect_Faulty_Windows) > max_data_count:
                                    del detect_Faulty_Windows[max_data_count:]

                                for index in range(len(detect_Faulty_Windows)):
                                    index2 = index % 4
                                    try:
                                        if str(df.at[detect, 'name']) in error_thresholds:
                                            Hata_Faultys_Window_labels[index2].setPixmap(QtGui.QPixmap.fromImage(detect_Faulty_Windows[index2]))
                                    except Exception as e:
                                        logging.error(f'Hata meydana geldi: {str(e)}')
                                        logging.error(f'Hatanın meydana geldiği kod satırı: {traceback.format_exc()}')
                                        pass
                                if str(df.iloc[:]['name'][detect])=='delik':
                                    detect_faulty_fabric["Flawed Hole"] += 1
                                elif str(df.iloc[:]['name'][detect])=='leke':
                                    detect_faulty_fabric["Flawed Spot"] += 1
                                elif str(df.iloc[:]['name'][detect])=='kirik':
                                    detect_faulty_fabric["Flawed Crack"] += 1
                                waitKey(2)
                                postOut = cvtColor(crop, COLOR_BGR2RGB)
                                img = Image.fromarray(postOut, "RGB")
                                img_byte_arr = BytesIO()
                                img.save(img_byte_arr, format='PNG')
                                img_byte_arr = img_byte_arr.getvalue()
                                if len(helper.last_images)>=5:
                                    del helper.last_images[0]
                                    helper.last_images.append(crop)
                                else:
                                    helper.last_images.append(crop)
                                imwrite(Save_image, copy_model_image)
                                imwrite(Save_crop_image, crop)
                                waitKey(1)
                                Hata_Koordinant = [x1, x2, y1, y2]
                                Hata_Koordinant = ", ".join(str(coord) for coord in Hata_Koordinant)
                                
                                helper.append_db(df, detect, Save_image, str(src), str(x), str(y), str(xy), Dok_no, Kalite_no, Hata_Koordinant, cloth_width, faulty_meter)
                            if (str(df.at[detect, 'name']) in error_thresholds) and (theta_1_center <= cx <= theta_2_center) and (y_detect_1 == y_detect_2) and crack_ready == True:
                                faulty_cnt += 1     
                            if (str(df.at[detect, 'name']) in error_thresholds) and (theta_1_center <= cx <= theta_2_center) and (y_detect_1 == y_detect_2):
                                faulty_cnt += 1
                            if (str(df.at[detect, 'name']) in error_thresholds):
                                faulty_cnt_100 +=1
                            elif not (theta_1_center <= cx <= theta_2_center):
                                faulty_cnt = 0
                            if faulty_cnt >= detect_threshold:
                                MainWindow11.show()
                                faulty_cnt = 0
                                Arduino_Tools.kirmizi_led_ac()
                                sleep(1./5)
                                Arduino_Tools.setBrightness(str(brightnessValue))
                                sleep(1./5)
                                Arduino_Tools.setBrightness(str(brightnessValue))
                                print("Kırmızı Led Aktif")
                            if faulty_cnt_100 >= detect_threshold_100:
                                MainWindow11.show()
                                faulty_cnt_100 = 0
                                print("Sari Led Aktif")
                                Arduino_Tools.sari_led_ac()
                                sleep(1./5)
                                Arduino_Tools.setBrightness(str(brightnessValue))
                                sleep(1./5)
                                Arduino_Tools.setBrightness(str(brightnessValue))
                            if Tools.Trigg_Port_Button==True:
                                try:
                                    src, speed = Arduino_Tools.Feedback_src()
                                    src: int = int(int(src) / 1000)
                                    speed: int = int(speed)
                                except Exception as e:
                                    logging.error(f'Hata meydana geldi: {str(e)}')
                                    logging.error(f'Hatanın meydana geldiği kod satırı: {traceback.format_exc()}')
                                    ui2.statusbar.showMessage(" "*1 + "Seri Port Hatası Metre bilgileri 0 Olarak Ayarlandı", 1500)
                                    src=0
                            if str(df.iloc[:]['name'][detect]) not in ['delik', 'leke']:
                                if len(helper.last_images)>=5:
                                    del helper.last_images[0]
                                    helper.last_images.append(crop)
                                else:
                                    helper.last_images.append(crop)
                                detect_faulty_fabric["Other Errors"] += 1
                                imwrite(Save_image, copy_model_image)
                                imwrite(Save_crop_image, crop)
                                Hata_Koordinant = [x1, x2, y1, y2]
                                Hata_Koordinant = ", ".join(str(coord) for coord in Hata_Koordinant)
                                faulty_meter = int(round(width_converter.convert(cx) / 10, 2))
                                try:
                                    helper.append_db(df, detect, Save_image, str(src), str(x), str(y), str(xy), Dok_no, Kalite_no, Hata_Koordinant, cloth_width, faulty_meter)
                                except Exception as e:
                                    logging.error(f'Hata meydana geldi: {str(e)}')
                                    logging.error(f'Hatanın meydana geldiği kod satırı: {traceback.format_exc()}')
                                    theta_1_center = max(0, cx - threshold)
                                    theta_2_center = min(model_image.shape[1], cx + threshold)
                                    y_detect_2, single_frame, faulty_meter = y_detect(cy, theta_1_center, theta_2_center, cx)
                                    helper.append_db(df, detect, Save_image, str(src), str(x), str(y), str(xy), Dok_no, Kalite_no, Hata_Koordinant, cloth_width, faulty_meter)
                ui9.text_Detect_Delik.setText(str(detect_faulty_fabric["Flawed Hole"]))
                ui9.text_Detect_Leke.setText(str(detect_faulty_fabric["Flawed Spot"]))
                ui9.text_Detect_Diger.setText(str(detect_faulty_fabric["Other Errors"]))
                ui9.text_Detect_Kirik.setText(str(detect_faulty_fabric["Flawed Crack"]))
                if Arduino_Tools.warning_status == False:
                    ui9.Ikaz_Durum.setText("KAPALI")
                else:
                    ui9.Ikaz_Durum.setText("AÇIK")
                ################################################################################################
                current_time_faulty_cnt = time.time()
                current_time_faulty_cnt_100 = time.time()
                current_time_crack_cnt = time.time()
                
                if current_time_faulty_cnt - start_time_faulty_cnt >= limited_time_faulty:
                    faulty_cnt = 0
                    start_time_faulty_cnt = current_time_faulty_cnt
                if current_time_faulty_cnt_100 - start_time_faulty_cnt_100 >= limited_time_faulty_100:
                    faulty_cnt_100 = 0
                    start_time_faulty_cnt_100 = current_time_faulty_cnt_100
                if current_time_crack_cnt - start_time_crack_cnt >= limited_time_crack:
                    crack_ready = True
                    start_time_crack_cnt = current_time_crack_cnt
                ################################################################################################
                single_frame = resize(out,  width=1400)
                if model_name == Tools.Camera_Serial[0]:
                    qImg=QImage(single_frame,width_s,height_s,step_s,QImage.Format_RGB888)
                    ui2.Camera_1.setPixmap(QPixmap.fromImage(qImg))
                elif model_name == Tools.Camera_Serial[1]:
                    qImg=QImage(single_frame,width_s,height_s,step_s,QImage.Format_RGB888)
                    ui2.Camera_2.setPixmap(QPixmap.fromImage(qImg))
                elif model_name == Tools.Camera_Serial[2]:
                    qImg=QImage(single_frame,width_s,height_s,step_s,QImage.Format_RGB888)
                    ui2.Camera_2.setPixmap(QPixmap.fromImage(qImg))
                elif model_name == Tools.Camera_Serial[3]:
                    qImg=QImage(single_frame,width_s,height_s,step_s,QImage.Format_RGB888)
                    ui2.Camera_2.setPixmap(QPixmap.fromImage(qImg))
                ui2.label_8.setText(str(fps))
                if choise == "Record":
                    for detect in range(len(df.iloc[:]['name'])):
                        ui2.Kayit_pushButton_2.setDisabled(True)
                        record_now_day = helper.Db_path_time(choice="Now-Day")
                        save_image_record_path = "./Database"+"/"+helper.Db_path_time(choice="Now-Day")+"/"+"Cam"+"/"+"images"+"/"+ "ss"+ "/" + df.iloc[:]['name'][detect]+"-"+helper.Db_path_time(choice="Now-Time")+"-"+".jpg"
                        imwrite(save_image_record_path, copy_model_image)
                        imwrite(Save_crop_image, crop)

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
                results = model(tensor_temp.cpu().numpy(), size=2048)
                results.display(render=True)
                h = results.ims[0].shape[0] 
                out1= cvtColor(results.ims[0][0:int(h/2), :],COLOR_BGR2RGB)
                out2= cvtColor(results.ims[0][int(h/2):, :]  ,COLOR_BGR2RGB)
                # Kırpma işlemi için kullanılacak görüntünün kopyası
                results_2 = tensor_temp.cpu().numpy()
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
                        Save_crop_image = "./Database"+"/"+helper.Db_path_time(choice="Now-Day")+"/"+"Cam"+"/"+"images"+"/"+"cropped"+"/"+df.iloc[:]['name'][detect]+"-"+helper.Db_path_time(choice="Now-Time")+"-"+".jpg"
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
                                # Arduino_Tools.kirmizi_led_ac()
                                try:
                                    src, speed = Arduino_Tools.Feedback_src()
                                    src: int = int(int(src) / 1000)
                                    speed: int = int(speed)
                                except Exception as e:
                                    logging.error(f'Hata meydana geldi: {str(e)}')
                                    logging.error(f'Hatanın meydana geldiği kod satırı: {traceback.format_exc()}')
                                    ui2.statusbar.showMessage(" "*1 + "Seri Port Hatası Metre bilgileri 0 Olarak Ayarlandı", 1500)
                                    src=0
                            if Tools.Trigg_Port_Button==False:
                                    src=0
                            #Hata alanının bulunması
                            x=abs(x2-x1)
                            y=abs(y2-y1)
                            x = round(width_converter.convert(x), 2)
                            y = round(width_converter.convert(y), 2)
                            xy = round(x * y, 2)
                            if str(df.iloc[:]['name'][detect])=='delik' or str(df.iloc[:]['name'][detect])=='leke': # Hatanın Delik veya Leke olması durumunda
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
                                    imwrite(Save_crop_image, crop)
                                    faulty_meter = int(round(width_converter.convert(cx) / 10, 2))
                                    helper.append_db(df, detect, Save_image, str(src), str(x), str(y), str(xy), Dok_no, Kalite_no, Hata_Koordinant, cloth_width, faulty_meter)
                                        
                                if Tools.Trigg_Port_Button==True:
                                    # Arduino_Tools.kirmizi_led_ac()
                                    try:
                                        src, speed = Arduino_Tools.Feedback_src()
                                        src: int = int(int(src) / 1000)
                                        speed: int = int(speed)
                                    except Exception as e:
                                        logging.error(f'Hata meydana geldi: {str(e)}')
                                        logging.error(f'Hatanın meydana geldiği kod satırı: {traceback.format_exc()}')
                                        ui2.statusbar.showMessage(" "*1 + "Seri Port Hatası Metre bilgileri 0 Olarak Ayarlandı", 1500)
                                        src=0
        
                            if not str(df.iloc[:]['name'][detect])=='delik' or not str(df.iloc[:]['name'][detect])=='leke':
                                if not helper.check_similarity(crop):
                                    if len(helper.last_images)>=5:
                                        del helper.last_images[0]
                                        helper.last_images.append(crop)
                                    else:
                                        helper.last_images.append(crop)
                                    imwrite(Save_image, results_2)
                                    imwrite(Save_crop_image, crop)
                                    faulty_meter = int(round(width_converter.convert(cx) / 10, 2))
                                    helper.append_db(df, detect, Save_image, str(src), str(x), str(y), str(xy), Dok_no, Kalite_no, Hata_Koordinant, cloth_width, faulty_meter)
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
            if len(frames) == 3:
                Dok_no= ui2.lineEdit_Dok_No.text()
                Kalite_no= ui2.comboBox_Kalite_No.currentText()
                frame, frame2, frame3 = frames[0][0], frames[1][0], frames[2][0]
                frame = frame[:-1, :-1, :]
                frame2 = frame2[:-1, :-1, :]
                frame3 = frame3[:-1, :-1, :]
                ImgPr1 = ImageProcessor(image=frame, trim_size=115, choise="left")
                ImgPr2 = ImageProcessor(image=frame2, trim_size=115)
                ImgPr3 = ImageProcessor(image=frame3, trim_size=115, choise="right")
                
                frame, cloth_width_1 = ImgPr1.trim_image()
                frame3, cloth_width_3 = ImgPr3.trim_image()
                try:
                    cloth_width_1 = round(width_converter.convert(cloth_width_1), 2)
                except Exception as e:
                    logging.error(f'Hata meydana geldi: {str(e)}')
                    logging.error(f'Hatanın meydana geldiği kod satırı: {traceback.format_exc()}')
                    cloth_width_1 = 0

                try:
                    cloth_width_2 = round(width_converter.convert(resolution_pixels_width), 2)
                except Exception as e:
                    logging.error(f'Hata meydana geldi: {str(e)}')
                    logging.error(f'Hatanın meydana geldiği kod satırı: {traceback.format_exc()}')
                    cloth_width_2 = 0
                try:
                    cloth_width_3 = round(width_converter.convert(cloth_width_3), 2)
                except Exception as e:
                    logging.error(f'Hata meydana geldi: {str(e)}')
                    logging.error(f'Hatanın meydana geldiği kod satırı: {traceback.format_exc()}')
                    cloth_width_3 = 0
                cloth_width = int((cloth_width_1 + cloth_width_2 + cloth_width_3) / 10)

                frame_model, frame2_model, frame3_model = frames[0][1], frames[1][1], frames[2][1]
                height, width, channel = frame.shape
                height2, width2, channel2 = frame2.shape
                height3, width3, channel3 = frame3.shape
                if ui2.radioButton_Camera_I.isChecked()==True and frame_model == Tools.Camera_Serial[0]:
                    configs[1]['value5'] = Tools.zoom_value_5()
                    configs[1]['value3'] = Tools.zoom_value_3()
                    configs[1]['value1'] = Tools.zoom_value_1()
                if ui2.radioButton_Camera_II.isChecked()==True and frame2_model == Tools.Camera_Serial[1]:
                    configs[2]['value5'] = Tools.zoom_value_5()
                    configs[2]['value3'] = Tools.zoom_value_3()
                    configs[2]['value1'] = Tools.zoom_value_1()
                if ui2.radioButton_Camera_III.isChecked()==True and frame3_model == Tools.Camera_Serial[2]:
                    configs[3]['value5'] = Tools.zoom_value_5()
                    configs[3]['value3'] = Tools.zoom_value_3()
                    configs[3]['value1'] = Tools.zoom_value_1()
                frame = frame[configs[1]['value5'][1]+ configs[1]['value3']: -configs[1]['value5'][1]+height  + configs[1]['value3'], configs[1]['value5'][0]+configs[1]['value1'] : width - (configs[1]['value5'][0])+ configs[1]['value1']]
                frame2 = frame2[configs[2]['value5'][1]+ configs[2]['value3']: -configs[2]['value5'][1]+height2  + configs[2]['value3'], configs[2]['value5'][0]+configs[2]['value1'] : width2 - (configs[2]['value5'][0])+ configs[2]['value1']]
                frame3 = frame3[configs[3]['value5'][1]+ configs[3]['value3']: -configs[3]['value5'][1]+height3  + configs[3]['value3'], configs[3]['value5'][0]+configs[3]['value1'] : width3 - (configs[3]['value5'][0])+ configs[3]['value1']]
                tensor1 = tensor(frame, device="cuda")
                tensor2 = tensor(frame2, device="cuda")
                tensor3 = tensor(frame3, device="cuda")
                new_frame_time = time.time()
                fps = 1/(new_frame_time-prev_frame_time)
                prev_frame_time = new_frame_time
                fps = int(fps)
                fps = str(fps)
                myTime+=1
                tensor_temp = cat([tensor1, tensor2, tensor3], dim=0)
                results = model(tensor_temp.cpu().numpy(), size=2048)
                df=results.pandas().xyxy[0]
                df=DataFrame(df)
                obj_df = []
                for obj_class_ai, threshold_ai in class_thresholds.items():
                    obj_df = df[(df['confidence'] >= threshold_ai) & (df['name'] == obj_class_ai)]
                    if not obj_df.empty:
                        results.render()
                h = results.ims[0].shape[0] 
                out1= cvtColor(results.ims[0][0:int(h/3), :],COLOR_BGR2RGB)
                out2= cvtColor(results.ims[0][int(h/3):int(2*h/3), :]  ,COLOR_BGR2RGB)
                out3= cvtColor(results.ims[0][int(2*h/3):int(h), :]  ,COLOR_BGR2RGB)
                waitKey(2)
                # Kırpma işlemi için kullanılacak görüntünün kopyası
                results_2 = tensor_temp.cpu().numpy()
                height, width, channel=out1.shape
                height2, width2, channel2=out2.shape
                height3, width3, channel3=out3.shape
                step=channel*width
                outs = [[out1, frame_model], [out2, frame2_model], [out3, frame3_model]]
                
                # Hataların koordinatları
                
                myTime+=1
                def y_detect(cy, theta_1_center, theta_2_center, cx):
                    if 0 <= cy <= frame.shape[0] * 1:
                        detect_cam = 1
                        cv2.line(out1, (int(theta_1_center), (detect_cam-1) * height), (int(theta_1_center), height*detect_cam), (0, 255, 0), thickness=2)
                        cv2.line(out1, (int(theta_2_center), (detect_cam-1) * height), (int(theta_2_center), height*detect_cam), (0, 255, 0), thickness=2)      
                        faulty_meter = round(width_converter.convert(cx) / 10, 2)
                        return detect_cam, out1, faulty_meter
                    elif frame.shape[0] * 1 < cy <= frame.shape[0] * 2:
                        detect_cam = 2
                        cv2.line(out2, (int(theta_1_center), (detect_cam-1) * height), (int(theta_1_center), height*detect_cam), (0, 255, 0), thickness=2)
                        cv2.line(out2, (int(theta_2_center), (detect_cam-1) * height), (int(theta_2_center), height*detect_cam), (0, 255, 0), thickness=2)      
                        faulty_meter = round(width_converter.convert(cx + width) / 10, 2) 
                        return detect_cam, out2, faulty_meter
                    elif frame.shape[0] * 2 < cy <= frame.shape[0] * 3:
                        detect_cam = 3
                        cv2.line(out3, (int(theta_1_center), (detect_cam-1) * height), (int(theta_1_center), height*detect_cam), (0, 255, 0), thickness=2)
                        cv2.line(out3, (int(theta_2_center), (detect_cam-1) * height), (int(theta_2_center), height*detect_cam), (0, 255, 0), thickness=2)      
                        faulty_meter = round(width_converter.convert(cx + width * 2) / 10, 2)
                        return detect_cam, out3, faulty_meter
                def fault_meter_detect(cy, cx):
                    if 0 <= cy <= frame.shape[0] * 1:
                        faulty_meter = round(width_converter.convert(cx) / 10, 2)
                        return faulty_meter
                    elif frame.shape[0] * 1 < cy <= frame.shape[0] * 2:
                        faulty_meter = round(width_converter.convert(cx + width) / 10, 2)
                        return faulty_meter
                    elif frame.shape[0] * 2 < cy <= frame.shape[0] * 3:
                        faulty_meter = round(width_converter.convert(cx + width * 2) / 10, 2)
                        return faulty_meter
                    
                for obj_class_ai, threshold_ai in class_thresholds.items():
                    obj_df = df[(df['confidence'] >= threshold_ai) & (df['name'] == obj_class_ai)]
                    if not obj_df.empty:
                        if len(df)!=0 and int(speed) >= type_speed:
                            for detect in range(len(df.iloc[:]['name'])):
                                Save_image="./Database"+"/"+helper.Db_path_time(choice="Now-Day")+"/"+"Cam"+"/"+"images"+"/"+df.iloc[:]['name'][detect]+"-"+helper.Db_path_time(choice="Now-Time")+"-"+".jpg"
                                Save_crop_image = "./Database"+"/"+helper.Db_path_time(choice="Now-Day")+"/"+"Cam"+"/"+"images"+"/"+"cropped"+"/"+df.iloc[:]['name'][detect]+"-"+helper.Db_path_time(choice="Now-Time")+"-"+".jpg"
                                x1=int(df.iloc[:]['xmin'][detect])
                                x2=int(df.iloc[:]['xmax'][detect])
                                y1=int(df.iloc[:]['ymin'][detect])
                                y2=int(df.iloc[:]['ymax'][detect])
                                classId = df.iloc[:]['class'][detect]
                                cx = (x1 + x2)/ 2
                                cy = (y1 + y2)/ 2
                                new_x1, new_x2, new_y1, new_y2 = Tools.expand(results_2.shape, x1, x2, y1, y2, [5.5, 1.1])
                                try:
                                    crop = results_2[new_y1:new_y2,new_x1:new_x2]
                                except Exception as e:
                                    logging.error(f'Hata meydana geldi: {str(e)}')
                                    logging.error(f'Hatanın meydana geldiği kod satırı: {traceback.format_exc()}')
                                    crop = results_2[y1:y2, x1:x2]
                                if Tools.Trigg_Port_Button == True:
                                    try:
                                        src, speed = Arduino_Tools.Feedback_src()
                                        src: int = int(int(src) / 1000)
                                        speed: int = int(speed)
                                    except Exception as e:
                                        logging.error(f'Hata meydana geldi: {str(e)}')
                                        logging.error(f'Hatanın meydana geldiği kod satırı: {traceback.format_exc()}')
                                        ui2.statusbar.showMessage(" "*1 + "Seri Port Hatası Metre bilgileri 0 Olarak Ayarlandı", 1500)
                                        src=0
                                if Tools.Trigg_Port_Button==False:
                                    src=0
                                x = abs(x2-x1)
                                y = abs(y2-y1)
                                x = round(width_converter.convert(x), 2)
                                y = round(width_converter.convert(y), 2)
                                xy = round(x * y, 2)
                                if (str(df.at[detect, 'name']) in ['dikis']):
                                    start_time_crack_cnt = time.time()
                                    crack_ready = False

                                if (str(df.at[detect, 'name']) in ['delik', 'leke', 'kirik']):
                                    if faulty_cnt == 0:
                                        start_time_faulty_cnt = time.time()
                                        theta_1_center = max(0, cx - threshold)
                                        theta_2_center = min(width, cx + threshold)
                                        y_detect_1, single_frame, faulty_meter = y_detect(cy, theta_1_center, theta_2_center, cx)
                                        # print(f"yakalanan kamera: {y_detect_1}")
                                    y_detect_2, single_frame, faulty_meter = y_detect(cy, theta_1_center, theta_2_center, cx)
                                    if faulty_cnt_100 == 0:
                                        start_time_faulty_cnt_100 = time.time()
                                    faulty_meter = int(round(width_converter.convert(cx) / 10, 2))
                                    faulty_meter = int(fault_meter_detect(cy, cx))
                                    crop = resize_cv2(crop, (320,320), interpolation = INTER_CUBIC)
                                    single_frame = resize(single_frame,  width=1400)
                                    image2 = QtGui.QImage(crop.data, crop.shape[1], crop.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
                                    image3 = QtGui.QImage(single_frame.data, single_frame.shape[1], single_frame.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
                                    ui6.Goster_Label.setPixmap(QtGui.QPixmap.fromImage(image2))
                                    detect_images.insert(0, image2)
                                    detect_Faulty_Windows.insert(0, image3)
                                    show_images.insert(0, single_frame)
                                    detect_Hata_Eni.insert(0, str(x))
                                    detect_Hata_Boyu.insert(0, str(y))
                                    detect_Hata_Alan.insert(0, str(faulty_meter))
                                    detect_Hata_Metre.insert(0, str(src))
                                    detect_Hata_Sinif.insert(0, str(df.iloc[:]['name'][detect]))

                                    # detect_images için değişiklik
                                    if len(detect_images) > max_data_count:
                                        del detect_images[max_data_count:]
                                    for index in range(len(detect_images)):
                                        index2 = index % 6
                                        index3 = page_num[index2]
                                        try:
                                            Hata_Goster_labels[index2].setPixmap(QtGui.QPixmap.fromImage(detect_images[index3]))
                                            Hata_Eni_labels[index2].setText(detect_Hata_Eni[index3])
                                            Hata_Boyu_labels[index2].setText(detect_Hata_Boyu[index3])
                                            Hata_Alan_labels[index2].setText(detect_Hata_Alan[index3])
                                            Hata_Metre_Labels[index2].setText(detect_Hata_Metre[index3])
                                            Hata_Sinif_labels[index2].setText(detect_Hata_Sinif[index3])
                                        except Exception as e:
                                            logging.error(f'Hata meydana geldi: {str(e)}')
                                            logging.error(f'Hatanın meydana geldiği kod satırı: {traceback.format_exc()}')
                                            pass

                                    # detect_Faulty_Windows için değişiklik
                                    if len(detect_Faulty_Windows) > max_data_count:
                                        del detect_Faulty_Windows[max_data_count:]

                                    for index in range(len(detect_Faulty_Windows)):
                                        index2 = index % 4
                                        try:
                                            if (str(df.at[detect, 'name']) in error_thresholds):
                                                Hata_Faultys_Window_labels[index2].setPixmap(QtGui.QPixmap.fromImage(detect_Faulty_Windows[index2]))
                                        except Exception as e:
                                            logging.error(f'Hata meydana geldi: {str(e)}')
                                            logging.error(f'Hatanın meydana geldiği kod satırı: {traceback.format_exc()}')
                                            pass  
                                    if str(df.iloc[:]['name'][detect])=='delik':
                                        detect_faulty_fabric["Flawed Hole"] += 1
                                    elif str(df.iloc[:]['name'][detect])=='leke':
                                        detect_faulty_fabric["Flawed Spot"] += 1
                                    elif str(df.iloc[:]['name'][detect])=='kirik':
                                        detect_faulty_fabric["Flawed Crack"] += 1
                                    waitKey(2)
                                    postOut = cvtColor(crop, COLOR_BGR2RGB)
                                    img = Image.fromarray(postOut, "RGB")
                                    img_byte_arr = BytesIO()
                                    img.save(img_byte_arr, format='PNG')
                                    img_byte_arr = img_byte_arr.getvalue()
                                    if len(helper.last_images)>=5:
                                        del helper.last_images[0]
                                        helper.last_images.append(crop)
                                    else:
                                        helper.last_images.append(crop)
                                    imwrite(Save_image, results_2)
                                    imwrite(Save_crop_image, crop)
                                    waitKey(1)
                                    Hata_Koordinant = [x1, x2, y1, y2]
                                    Hata_Koordinant = ", ".join(str(coord) for coord in Hata_Koordinant)
                                    helper.append_db(df, detect, Save_image, str(src), str(x), str(y), str(xy), Dok_no, Kalite_no, Hata_Koordinant, cloth_width, faulty_meter)

                                if (str(df.at[detect, 'name']) in error_thresholds) and (theta_1_center <= cx <= theta_2_center) and (y_detect_1 == y_detect_2) and crack_ready == True:
                                    faulty_cnt += 1     
                                if (str(df.at[detect, 'name']) in error_thresholds) and (theta_1_center <= cx <= theta_2_center) and (y_detect_1 == y_detect_2):
                                    faulty_cnt += 1
                                if (str(df.at[detect, 'name']) in error_thresholds):
                                    faulty_cnt_100 +=1
                                elif not (theta_1_center <= cx <= theta_2_center):
                                    faulty_cnt = 0
                                if faulty_cnt >= detect_threshold:
                                    MainWindow11.show()
                                    faulty_cnt = 0
                                    Arduino_Tools.kirmizi_led_ac()
                                    sleep(1./5)
                                    Arduino_Tools.setBrightness(str(brightnessValue))
                                    sleep(1./5)
                                    Arduino_Tools.setBrightness(str(brightnessValue))
                                    print("Kırmızı Led Aktif")
                                if faulty_cnt_100 >= detect_threshold_100:
                                    MainWindow11.show()
                                    faulty_cnt_100 = 0
                                    print("Sari Led Aktif")
                                    Arduino_Tools.sari_led_ac()
                                    sleep(1./5)
                                    Arduino_Tools.setBrightness(str(brightnessValue))
                                    sleep(1./5)
                                    Arduino_Tools.setBrightness(str(brightnessValue))
                                if Tools.Trigg_Port_Button==True:
                                    try:
                                        src, speed = Arduino_Tools.Feedback_src()
                                        src: int = int(int(src) / 1000)
                                        speed: int = int(speed)
                                    except Exception as e:
                                        logging.error(f'Hata meydana geldi: {str(e)}')
                                        logging.error(f'Hatanın meydana geldiği kod satırı: {traceback.format_exc()}')
                                        ui2.statusbar.showMessage(" "*1 + "Seri Port Hatası Metre bilgileri 0 Olarak Ayarlandı", 1500)
                                        src=0
                                try:
                                    if str(df.iloc[:]['name'][detect]) not in ['delik', 'leke']:
                                        if len(helper.last_images)>=5:
                                            del helper.last_images[0]
                                            helper.last_images.append(crop)
                                        else:
                                            helper.last_images.append(crop)
                                        detect_faulty_fabric["Other Errors"] += 1
                                        imwrite(Save_image, results_2)
                                        imwrite(Save_crop_image, crop)
                                        Hata_Koordinant = [x1, x2, y1, y2]
                                        Hata_Koordinant = ", ".join(str(coord) for coord in Hata_Koordinant)
                                        try:
                                            helper.append_db(df, detect, Save_image, str(src), str(x), str(y), str(xy), Dok_no, Kalite_no, Hata_Koordinant, cloth_width, faulty_meter)
                                        except Exception as e:
                                            logging.error(f'Hata meydana geldi: {str(e)}')
                                            logging.error(f'Hatanın meydana geldiği kod satırı: {traceback.format_exc()}')
                                            theta_1_center = max(0, cx - threshold)
                                            theta_2_center = min(model_image.shape[1], cx + threshold)
                                            y_detect_2, single_frame, faulty_meter = y_detect(cy, theta_1_center, theta_2_center, cx)
                                            faulty_meter = int(round(width_converter.convert(cx) / 10, 2))
                                            helper.append_db(df, detect, Save_image, str(src), str(x), str(y), str(xy), Dok_no, Kalite_no, Hata_Koordinant, cloth_width, faulty_meter)
                                except Exception as e:
                                    logging.error(f'Hata meydana geldi: {str(e)}')
                                    logging.error(f'Hatanın meydana geldiği kod satırı: {traceback.format_exc()}')
                                    pass
                ui9.text_Detect_Delik.setText(str(detect_faulty_fabric["Flawed Hole"]))
                ui9.text_Detect_Leke.setText(str(detect_faulty_fabric["Flawed Spot"]))
                ui9.text_Detect_Diger.setText(str(detect_faulty_fabric["Other Errors"]))
                ui9.text_Detect_Kirik.setText(str(detect_faulty_fabric["Flawed Crack"]))
                if Arduino_Tools.warning_status == False:
                    ui9.Ikaz_Durum.setText("KAPALI")
                else:
                    ui9.Ikaz_Durum.setText("AÇIK")
                ###############################################################################################
                current_time_faulty_cnt = time.time()
                current_time_faulty_cnt_100 = time.time()
                current_time_crack_cnt = time.time()
                
                if current_time_faulty_cnt - start_time_faulty_cnt >= limited_time_faulty:
                    
                    faulty_cnt = 0
                    start_time_faulty_cnt = current_time_faulty_cnt
                if current_time_faulty_cnt_100 - start_time_faulty_cnt_100 >= limited_time_faulty_100:
                    faulty_cnt_100 = 0
                    start_time_faulty_cnt_100 = current_time_faulty_cnt_100
                if current_time_crack_cnt - start_time_crack_cnt >= limited_time_crack:
                    crack_ready = True
                    start_time_crack_cnt = current_time_crack_cnt
                frame_1 = resize(out1, width=1400)
                frame_2 = resize(out2, width=1400)
                frame_3 = resize(out3, width=1400)
                outs_show = [[frame_1, frame_model], [frame_2, frame2_model], [frame_3, frame3_model]]
                height_s, width_s, channel_s = outs_show[0][0].shape
                step_s = channel_s * width_s 
                for out in outs_show:
                    if out[1] == Tools.Camera_Serial[0]:
                        qImg=QImage(out[0],width_s,height_s,step_s,QImage.Format_RGB888)
                        ui2.Camera_1.setPixmap(QPixmap.fromImage(qImg))
                    if out[1] == Tools.Camera_Serial[1]:
                        qImg=QImage(out[0],width_s,height_s,step_s,QImage.Format_RGB888)
                        ui2.Camera_2.setPixmap(QPixmap.fromImage(qImg))
                    if out[1] == Tools.Camera_Serial[2]:
                        qImg=QImage(out[0],width_s,height_s,step_s,QImage.Format_RGB888)
                        ui2.Camera_3.setPixmap(QPixmap.fromImage(qImg))

                if choise == "Record":
                    ui2.Kayit_pushButton_2.setDisabled(True)
                    record_now_day = helper.Db_path_time(choice="Now-Day")
                    save_image_record_path = "./Database"+"/"+helper.Db_path_time(choice="Now-Day")+"/"+"Cam"+"/"+"images"+"/"+ "ss"+ "/" + df.iloc[:]['name'][detect]+"-"+helper.Db_path_time(choice="Now-Time")+"-"+".jpg"
                    imwrite(save_image_record_path, results_2)
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
        ui2.Kayit_pushButton_2.setDisabled(False)
        ui2.Off_pushButton.setDisabled(True)
        pixmap = QPixmap('./Icon/Label Img/CameraOFF.PNG')
        pixmap_detect_off = QPixmap('./Icon/Label Img/DetectOFF.PNG')
        last_detect(pixmap_detect_off)
        ui2.Camera_1.setPixmap(pixmap) 
        ui2.Camera_2.setPixmap(pixmap) 
        ui2.Camera_3.setPixmap(pixmap) 
        ui2.Camera_4.setPixmap(pixmap) 
        Tools.Non_Trigg_Port_Button=False
        Tools.Trigg_Port_Button=False
        ui2.label_9.setText(str(0))
        MainWindow9.close()
        for index in range(len(detect_images)):
            indexx = index % 6
            indexxx = page_num[indexx]
            try:
                Hata_Goster_labels[indexx].setPixmap(QtGui.QPixmap.fromImage(detect_images[indexxx]))
                Hata_Eni_labels[indexx].setText(detect_Hata_Eni[indexxx])
                Hata_Boyu_labels[indexx].setText(detect_Hata_Boyu[indexxx])
                Hata_Alan_labels[indexx].setText(detect_Hata_Alan[indexxx])
                Hata_Metre_Labels[indexx].setText(detect_Hata_Metre[indexxx])
                Hata_Sinif_labels[indexx].setText(detect_Hata_Sinif[indexxx])
            except Exception as e:
                logging.error(f'Hata meydana geldi: {str(e)}')
                logging.error(f'Hatanın meydana geldiği kod satırı: {traceback.format_exc()}')
                pass
        for index in range(len(detect_Faulty_Windows)):
            indexx = index % 4
            try:
                Hata_Faultys_Window_labels[indexx].setPixmap(QtGui.QPixmap.fromImage(detect_Faulty_Windows[index]))
            except Exception as e:
                logging.error(f'Hata meydana geldi: {str(e)}')
                logging.error(f'Hatanın meydana geldiği kod satırı: {traceback.format_exc()}')
                pass    
    ## Çıkış Buttonu

    ########################################################################################################################
    def Close():
        Arduino_Tools.hepsini_kapat()
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
                        mkdir(day_db_is_here+"/"+now+"/"+"Cam"+"/"+"images"+"/"+"cropped")
                        mkdir(day_db_is_here+"/"+now+"/"+"Cam"+"/"+"images"+"/"+"ss")
                        mkdir(day_db_is_here+"/"+now+"/"+"Cam"+"/"+"videos")
                        break
                    except Exception as e:
                        logging.error(f'Hata meydana geldi: {str(e)}')
                        logging.error(f'Hatanın meydana geldiği kod satırı: {traceback.format_exc()}')
                        print("Klasör Zaten var")
                        ui2.statusbar.showMessage(" "*1 + " Yerel veri tabanı klasörü zaten bulunmaktadır...", 1500)
                        break
    ########################################################################################################################
    def starting_upload():
        Tools.default_upload()
        configs[1] = Tools.feedback_js()['1']
        configs[2] = Tools.feedback_js()['2']
        configs[3] = Tools.feedback_js()['3']
        configs[4] = Tools.feedback_js()['4']

    def default_model():
        path = Veri_Tabani_Window().get_last_model_path()
        Tools.Model_Path = path
        
    def Upload_Cameras_Inf():
        _Camera_Height, _Camera_Width, _Camera_Impact_Rate, _Camera_Serial, _Camera_Exposure_Time, _Camera_Cut_Off, _Cameras_Type= Tools.feedback_Splited_Last_Data()
        Veri_Tabani_Window().Last_Cameras_Info_Add(_Camera_Height, _Camera_Width, _Camera_Impact_Rate, _Camera_Serial, _Camera_Exposure_Time, _Camera_Cut_Off, _Cameras_Type,
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

    def Camera_Inf():
        Tools.Import_Height()
        Tools.Import_Width()
        Tools.Import_Camera_Serial()
        Tools.Import_Camera_Exposure_Time()
        Tools.Import_Cameras_Type()

    def last_detect(pixmap_detect_off):
        ui9.label_Hata_Goster_1.setPixmap(pixmap_detect_off)
        ui9.label_Hata_Goster_2.setPixmap(pixmap_detect_off)
        ui9.label_Hata_Goster_3.setPixmap(pixmap_detect_off)
        ui9.label_Hata_Goster_4.setPixmap(pixmap_detect_off)
        ui9.label_Hata_Goster_5.setPixmap(pixmap_detect_off)
        ui9.label_Hata_Goster_6.setPixmap(pixmap_detect_off)  

    def getbrightness():
        brightnessValue = ui5.horizontal_Isik_siddeti.value() 
        Arduino_Tools.setBrightness(brightnessValue)
        ui5.label_Kumas_Turu_2.setText("Işık Şiddeti " + f" {brightnessValue}")
        if brightnessValue == 0:
           ui5.label_Kumas_Turu_2.setText("Işık Şiddeti")

    def arduinoAdminConnect():
        Arduino_Tools.port_ac_yerel(Tools) 
        ui5.pushButton_Baglan.setDisabled(True)
        ui5.pushButton_Kapat.setDisabled(False)

    def arduinoAdminDisconnect():
        Arduino_Tools.hepsini_kapat()
        Arduino_Tools.port_kapat()
        ui5.pushButton_Baglan.setDisabled(False)
        ui5.pushButton_Kapat.setDisabled(True)
    
    def save_fabric_adjustment():
        save_fabric_classification = ui5.lineEdit_Kumas_Turu.text()
        save_fabric_light_level = ui5.horizontal_Isik_siddeti.value()
        Veri_Tabani_Window().set_fabric_settings(save_fabric_classification, save_fabric_light_level)
        for fabric_name in Veri_Tabani_Window().get_fabric_name():
            if ui2.comboBox_Kalite_No.findText(fabric_name) == -1:
                ui2.comboBox_Kalite_No.addItem(fabric_name)
    def warning_status_inf():
        Arduino_Tools.hepsini_kapat()
        Arduino_Tools.warning_status = False
    def show_faulty(name:str = None, arr:np.ndarray = None):
        cv2.destroyAllWindows()
        scale = 1.0
        h, w = arr.shape[:2]
        res = np.zeros((h, w, 3), dtype=np.uint8)

        def zoom_in(x, y):
            nonlocal scale, res
            scale *= 1.2
            res = cv2.resize(arr, (0, 0), fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)
            cv2.imshow(name, res)

        def zoom_out(x, y):
            nonlocal scale, res
            scale /= 1.2
            res = cv2.resize(arr, (0, 0), fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)
            cv2.imshow(name, res)

        def zoom_reset(x, y):
            nonlocal scale, res
            scale = 1.0
            res = arr.copy()
            cv2.imshow(name, res)

        def mouse_callback(event, x, y, flags, params):
            if event == cv2.EVENT_LBUTTONDOWN:
                zoom_in(x, y)
            elif event == cv2.EVENT_RBUTTONDOWN:
                zoom_out(x, y)
            elif event == cv2.EVENT_MBUTTONDOWN:
                zoom_reset(x, y)

        cv2.imshow(name, arr)
        cv2.setMouseCallback(name, mouse_callback)
        cv2.waitKey(1)

    def faulty_close():
        MainWindow11.close()
        warning_status_inf()

    def closeEvent(event, choice):
            reply = QMessageBox.question(choice, 'Pencere Kapatma', 'Pencereyi kapatmak istediğinize emin misiniz?',
                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                event.accept()
                _exit(0)
            else:
                event.ignore()
    def camera_local_inf():
        local_height = int(ui5.lineEdit_Kamera_Yuksekligi.text()) if ui5.lineEdit_Kamera_Yuksekligi.text().isdigit() else 200
        vision_weight = int(ui5.lineEdit_Kamera_Gorus_Genisligi.text()) if ui5.lineEdit_Kamera_Gorus_Genisligi.text().isdigit() else 200
        vision_height = int(ui5.lineEdit_Kamera_Gorus_Yuksekligi.text()) if ui5.lineEdit_Kamera_Gorus_Yuksekligi.text().isdigit() else 200
        vision_angle = int(ui5.lineEdit_Kamera_Gorus_Acisi.text()) if ui5.lineEdit_Kamera_Gorus_Acisi.text().isdigit() else 200
        Veri_Tabani_Window().set_Camera_Local_Settings(local_height, vision_weight, vision_height, vision_angle)
    def faulty_window_cnt_plus():
        nonlocal page_cnt
        nonlocal page_num
        page_cnt_copy = page_cnt
        page_cnt = page_cnt + 1
        if page_cnt >= len(detect_images) /6:
            page_cnt = page_cnt_copy
        page_start = (page_cnt - 1) * 6
        page_end = page_start + 6
        page_num = list(range(page_start, page_end))
        # print(page_num)
    def faulty_window_cnt_diff():
        nonlocal page_cnt
        nonlocal page_num
        page_cnt = page_cnt - 1
        if page_cnt == 0:
            page_cnt = 1
        page_start = (page_cnt - 1) * 6
        page_end = page_start + 6
        page_num = list(range(page_start, page_end))
        # print(page_num)
    def faulty_window_cnt_home():
        nonlocal page_cnt
        nonlocal page_num
        page_cnt = 1
        page_start = (page_cnt - 1) * 6
        page_end = page_start + 6
        page_num = list(range(page_start, page_end))
        # print(page_num)
    def faulty_window():
        for index in range(6):
            index2 = index % 6
            index3 = page_num[index2] 
            try:
                # print(index3)
                Hata_Goster_labels[index2].setPixmap(QtGui.QPixmap.fromImage(detect_images[index3]))
                Hata_Eni_labels[index2].setText(detect_Hata_Eni[index3])
                Hata_Boyu_labels[index2].setText(detect_Hata_Boyu[index3])
                Hata_Alan_labels[index2].setText(detect_Hata_Alan[index3])
                Hata_Metre_Labels[index2].setText(detect_Hata_Metre[index3])
                Hata_Sinif_labels[index2].setText(detect_Hata_Sinif[index3])
            except Exception as e:
                logging.error(f'Hata meydana geldi: {str(e)}')
                logging.error(f'Hatanın meydana geldiği kod satırı: {traceback.format_exc()}')
                pass
    def mail_listwidget():
        # mail_listWidget'ı temizle
        email_data = Veri_Tabani_Window().mail_show()
        ui5.mail_listWidget.clear()
        for i, email in enumerate(email_data):
            if i == 0:
                ui12.lineEdit_gnderici_adres.setText(email[0])
            else:
                ui12.mail_kayitli_adresler.addItem(email[0])
            ui5.mail_listWidget.addItem(email[0])
    def mail_deleted():
        selected_item = ui5.mail_listWidget.selectedItems()
        try:
            select_item = ui5.mail_listWidget.currentItem().text()
        except AttributeError:
            select_item = None
        Veri_Tabani_Window().mail_delete(select_item)
        for item in selected_item:
            ui5.mail_listWidget.takeItem(ui5.mail_listWidget.row(item))

    def mail_add():
        item = ui5.lineEdit_mail.text()
        Veri_Tabani_Window().mail_add(item)
        ui5.mail_listWidget.addItem(item)

    def right_add():
        try:
            selected_item = ui12.mail_kayitli_adresler.currentItem()
            index = ui12.mail_kayitli_adresler.row(selected_item)
            ui12.mail_kayitli_adresler.takeItem(index)
            ui12.mail_gnderilen_adresler.addItem(selected_item.text())
        except Exception as e:
            logging.error(f'Hata meydana geldi: {str(e)}')
            logging.error(f'Hatanın meydana geldiği kod satırı: {traceback.format_exc()}')
            pass
        
    def left_add():
        try:
            selected_item = ui12.mail_gnderilen_adresler.currentItem()
            index = ui12.mail_gnderilen_adresler.row(selected_item)
            ui12.mail_gnderilen_adresler.takeItem(index)
            ui12.mail_kayitli_adresler.addItem(selected_item.text())
        except Exception as e:
            logging.error(f'Hata meydana geldi: {str(e)}')
            logging.error(f'Hatanın meydana geldiği kod satırı: {traceback.format_exc()}')
            pass

    def mail_send():
        mail_data, key_data = Veri_Tabani_Window().mail_key_show()
        listWidget = ui12.mail_gnderilen_adresler
        mail_list = []
        for index in range(listWidget.count()):
            item = listWidget.item(index)
            mail_list.append(item.text())
        email_sender = EmailSender.get_instance()
        email_sender.send_email(ui12, mail_data, key_data, mail_list, out_pdf_path, "Günlük hata tespiti ektedir")
    
    def Pdf_Lister():
        DC.ui3.Listele_pushButton.setEnabled(False)
        DC.ui3.Raporla_PushButton.setEnabled(False)
        inf_pdf = Vtw.get_details()
        # MainWindow12.show()
        widget_1 = DC.ui3.calendarWidget.selectedDate()
        widget_2 = DC.ui3.calendarWidget_2.selectedDate()
        Date = [str(widget_1.day()), str(widget_1.month()), str(widget_1.year())]
        DateLast = [str(widget_2.day()), str(widget_2.month()), str(widget_2.year())]
        def handle_out_path_main_callback(out_path_main):
            nonlocal out_pdf_path
            print(f"out_path_main: {out_path_main}")
            out_pdf_path = out_path_main
        mail_sender_Window(Date, DateLast, MainWindow12, inf_pdf, handle_out_path_main_callback)
        Vtw.set_details()
    
    def pdf_filter():
        DC.ui3.Raporla_PushButton.setEnabled(True)
        DC.ui3.Listele_pushButton.setEnabled(True)
        Vtw.filter()
    print("Arayüzlerin Yüklenmesi")
    worker.progress.emit(83)
    Arduino_Tools=Arduino_Toolkits()
    print("Arduino Toolkit Yüklendi")
    worker.progress.emit(86)
    Tools=ToolKit()
    print("Toolkit Yüklendi")
    worker.progress.emit(90)
    helper = Helper().start()
    print("Helper Yüklendi")
    worker.progress.emit(93)
    post_reader = post_thread()
    print("Mobil araçları Yüklendi")
    worker.progress.emit(96)
    post_reader.post_thread_start()
    worker.progress.emit(98)
    model = get_model(Tools)
    print("Yapay Zeka Yüklendi")
    worker.progress.emit(99)
    ################################################ Giris ################################################
    MainWindow1,MainWindow2,MainWindow3,MainWindow4,MainWindow5=Tools.FeedBack_Windows()
    ui1,ui2,ui3,ui4,ui5=Tools.FeedBack_SetupUi()
    app1,app2,app3,app4,app5=Tools.FeedBack_App()
    zoom_impact_rate=Tools.FeedBack_Zoom_Rate()
    app6,MainWindow6,ui6=Arduino_Tools.FeedBack_MainWindow_Error()
    ui7, MainWindow7, app7 = Tools.FeedBack_Port_UI()
    ui8, MainWindow8, app8 = Tools.Feedback_Kayt_UI()
    ui9, MainWindow9, app9 = Tools.Feedback_Faulty_UI()
    ui10, MainWindow10, app10 = Tools.FeedBack_Warning_UI()
    ui11, MainWindow11, app11 = Tools.FeedBack_Faultys_UI()
    ui12, MainWindow12, app12 = Tools.FeedBack_Mail_UI()
    #######################################################################################################
    inf_pdf = []
    Vtw = Veri_Tabani_Window()
    max_data_count = 500
    black_image = np.zeros((256, 1400), dtype=np.uint8)
    show_images       = [black_image, black_image, black_image, black_image, black_image, black_image]
    detect_images     = []
    detect_Hata_Eni   = []
    detect_Hata_Boyu  = []
    detect_Hata_Alan  = []
    detect_Hata_Metre = []
    detect_Hata_Sinif = []
    detect_Faulty_Windows = []
    Hata_Goster_labels = [ui9.label_Hata_Goster_1, ui9.label_Hata_Goster_2, ui9.label_Hata_Goster_3,
                              ui9.label_Hata_Goster_4, ui9.label_Hata_Goster_5, ui9.label_Hata_Goster_6]
    Hata_Eni_labels =    [ui9.text_Hata_Eni_1, ui9.text_Hata_Eni_2, ui9.text_Hata_Eni_3,
                            ui9.text_Hata_Eni_4, ui9.text_Hata_Eni_5, ui9.text_Hata_Eni_6]
    Hata_Boyu_labels =   [ui9.text_Hata_Boyu_1, ui9.text_Hata_Boyu_2, ui9.text_Hata_Boyu_3,
                            ui9.text_Hata_Boyu_4, ui9.text_Hata_Boyu_5, ui9.text_Hata_Boyu_6]
    Hata_Alan_labels =   [ui9.text_Hata_Alan_1, ui9.text_Hata_Alan_2, ui9.text_Hata_Alan_3,
                            ui9.text_Hata_Alan_4, ui9.text_Hata_Alan_5, ui9.text_Hata_Alan_6]
    Hata_Metre_Labels =  [ui9.Metre_Label_1, ui9.Metre_Label_2, ui9.Metre_Label_3,
                            ui9.Metre_Label_4, ui9.Metre_Label_5, ui9.Metre_Label_6]
    Hata_Sinif_labels =  [ui9.text_Hata_Sinif_1, ui9.text_Hata_Sinif_2, ui9.text_Hata_Sinif_3,
                            ui9.text_Hata_Sinif_4, ui9.text_Hata_Sinif_5, ui9.text_Hata_Sinif_6]
    Hata_Faultys_Window_labels = [ui11.fault_1_label, ui11.fault_2_label, ui11.fault_3_label]
    page_cnt = 1
    page_num = [0, 1, 2, 3, 4, 5]
    out_pdf_path = ""
    #######################################################################################################
    
    worker.progress.emit(100)
    time.sleep(0.5)
    window.close()
    worker.finished.emit()
    helper.pdf_folder_create()
    MainWindow1.show()
    Tools.Cam_out_file_folder()
    New_Day_Folder()
    Veri_Tabani_Window().Listele()
    Veri_Tabani_Window().get_last_path()
    Veri_Tabani_Window().get_last_Heigt_Width()
    ui2.logic_All = 0
    ui2.Off_pushButton.setDisabled(True)
    pixmap = QPixmap('./Icon/Label Img/CameraOFF.PNG')
    pixmap_detect_off = QPixmap('./Icon/Label Img/DetectOFF.PNG')
    ui2.Camera_1.setPixmap(pixmap) 
    ui2.Camera_2.setPixmap(pixmap) 
    ui2.Camera_3.setPixmap(pixmap) 
    ui2.Camera_4.setPixmap(pixmap) 
    last_detect(pixmap_detect_off)
    starting_upload()
    default_model()
    mail_listwidget()
    timer = QTimer()
    timer.timeout.connect(showTime)
    timer.start(1000)
    for fabric_name in Veri_Tabani_Window().get_fabric_name():
        ui2.comboBox_Kalite_No.addItem(fabric_name)
    ##Slotlar
    #######################
    get_log_reg=GirisVKayit(app1, ui1, ui2, ui8, MainWindow1, MainWindow2, MainWindow8, MainWindow9, Veri_Tabani_Window().get_users_inf(), Veri_Tabani_Window)
    ui1.actionClose.triggered.connect(Close)
    ui1.Giris_pushButton.clicked.connect(lambda : get_log_reg.Giris("Camera"))
    ui1.Kayit_pushButton.clicked.connect(lambda : get_log_reg.Giris("Kayit"))
    # ui2.Start_pushButton.clicked.connect(Video_Selected)
    ui2.Stop_pushButton.clicked.connect(Click_Button_Stop)
    ui2.Off_pushButton.clicked.connect(Click_Button_All_Stop)
    ui2.Close_pushButton.clicked.connect(Close)
    ui2.Ac_pushButton.clicked.connect(displayImage)
    ui2.Kayit_pushButton_2.clicked.connect(record_cameras_data)
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
    ui2.actionHata.triggered.connect(Tools.QWindow_Hata_Paneli)

    
    DC.ui3.action_k.triggered.connect(Close)
    DC.ui3.actionKameralar.triggered.connect(Tools.QWindow_Camera)
    DC.ui3.actionAdmin_Paneli.triggered.connect(Tools.QWindow_Admin)
    DC.ui3.Temiz_pushButton.clicked.connect(Veri_Tabani_Window().Clear)
    DC.ui3.Veri_Tabani_Widget.itemSelectionChanged.connect(Veri_Tabani_Window().Doldur)
    DC.ui3.Goster_pushButton.clicked.connect(Veri_Tabani_Window().Ara)
    DC.ui3.Raporla_PushButton.clicked.connect(Pdf_Show)
    DC.ui3.Listele_pushButton.clicked.connect(Pdf_Lister)
    DC.ui3.Filtrele_pushButton.clicked.connect(pdf_filter)
    DC.ui3.Gunclle_PushButton.clicked.connect(Veri_Tabani_Window().Update)
    DC.ui3.Delete_PushButton.clicked.connect(Veri_Tabani_Window().Delete)
    DC.ui4.Ikaz_kapat_pushButton.clicked.connect(lambda: DC.MainWindow4.close())
    
    ui5.action_k.triggered.connect(Close)
    ui5.pushButton_Find_File.clicked.connect(Tools.getFile)
    ui5.pushButton_Aktar_Ysa.clicked.connect(Tools.Import_Model)
    ui5.pushButton_Aktar_Kamera.clicked.connect(Camera_Inf)
    ui5.pushButton_Aktar_Serial_Port.clicked.connect(Tools.Import_Serial_Port)
    ui5.pushButton_Upload.clicked.connect(Upload_Cameras_Inf)
    ui5.actionKameralar.triggered.connect(Tools.QWindow_Camera)
    ui5.actionVeri_Taban.triggered.connect(Tools.QWindow_DataBase)
    ui5.horizontal_Isik_siddeti.valueChanged.connect(getbrightness)
    ui5.pushButton_Baglan.clicked.connect(arduinoAdminConnect)
    ui5.pushButton_Kapat.clicked.connect(arduinoAdminDisconnect)
    ui5.pushButton_Aktar_Kumas_Inf.clicked.connect(save_fabric_adjustment)
    ui5.pushButton_Kamera_Konum_Ayari.clicked.connect(camera_local_inf)
    ui5.pushButton_mail_sil.clicked.connect(mail_deleted)
    ui5.pushButton_mail_ekle.clicked.connect(mail_add)
    ui6.Ikaz_kapat_pushButton.clicked.connect(Arduino_Tools.hepsini_kapat)
    # ui7.Ac_pushButton.clicked.connect(Soft_Serial_OPEN)
    ui7.Kapat_pushButton.clicked.connect(Soft_NSerial_OPEN)
    ui8.Giris_pushButton.clicked.connect(lambda : get_log_reg.kayit())
    ui8.action_k.triggered.connect(Close)
    ui9.ikaz_button.clicked.connect(warning_status_inf)
    ui9.system_close.clicked.connect(Click_Button_All_Stop)
    ui9.actionKameralar.triggered.connect(Tools.QWindow_Camera)
    ui9.actionVeri_Taban.triggered.connect(Tools.QWindow_DataBase)
    ui9.actionAdmin_Paneli.triggered.connect(Tools.QWindow_Admin)
    try:
        ui9.label_Hata_Goster_1.mousePressEvent = lambda event: show_faulty(name="Hata - 1", arr=show_images[page_num[0]])
        ui9.label_Hata_Goster_2.mousePressEvent = lambda event: show_faulty(name="Hata - 2", arr=show_images[page_num[1]])
        ui9.label_Hata_Goster_3.mousePressEvent = lambda event: show_faulty(name="Hata - 3", arr=show_images[page_num[2]])
        ui9.label_Hata_Goster_4.mousePressEvent = lambda event: show_faulty(name="Hata - 4", arr=show_images[page_num[3]])
        ui9.label_Hata_Goster_5.mousePressEvent = lambda event: show_faulty(name="Hata - 5", arr=show_images[page_num[4]])
        ui9.label_Hata_Goster_6.mousePressEvent = lambda event: show_faulty(name="Hata - 6", arr=show_images[page_num[5]])
    except Exception as e:
        logging.error(f'Hata meydana geldi: {str(e)}')
        logging.error(f'Hatanın meydana geldiği kod satırı: {traceback.format_exc()}')
        print("Maksimum alan aşı")
    ui10.Kapat_pushButton.clicked.connect(lambda: MainWindow10.close())
    ui11.close_pushButton.clicked.connect(faulty_close)
    MainWindow2.closeEvent = lambda event: closeEvent(event=event, choice=MainWindow2)
    ui9.righr_pushButton.clicked.connect(faulty_window_cnt_plus)
    ui9.left_pushButton.clicked.connect(faulty_window_cnt_diff)
    ui9.home_pushButton.clicked.connect(faulty_window_cnt_home)
    ui9.righr_pushButton.clicked.connect(faulty_window)
    ui9.left_pushButton.clicked.connect(faulty_window)
    ui9.home_pushButton.clicked.connect(faulty_window)
    ui12.aktargnderlen_pushButton.clicked.connect(right_add)
    ui12.aktarkayitli_pushButton.clicked.connect(left_add)
    ui12.mailgonder_pushButton.clicked.connect(mail_send)


def check_if_process_running(process_name):
    """
    Kontrol etmek istediğiniz süreç isminin ne kadar çalıştığını döndüren fonksiyon.
    """
    try:
        # Tüm süreçleri gezip istenilen süreci sayar
        count = 0
        for proc in psutil.process_iter():
            process = proc.as_dict(attrs=['pid', 'name'])
            if process_name in process['name']:
                count += 1
        return count
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
        logging.error(f"Process kontrolü sırasında hata: {e}")
        pass

    
if __name__ == '__main__':
    # "menderesapp" adında bir sürecin çalışıp çalışmadığını kontrol et
    with open("./configs/name key.txt", "r") as file:
        name = file.readline().strip()
    process_count = check_if_process_running(name)
    logging.info(f"'{name}' sürecinin çalışma sayısı: {process_count}")
    if process_count > 1:
        logging.warning(f"{name} süreci zaten çalışıyor. Uygulama sonlandırılıyor.")
        sys.exit(1)  # Eğer 1'den fazla süreç çalışıyorsa uygulamayı sonlandır.
    app1 = QApplication(sys.argv)
    window = MainWindow()
    app1.exec_()







