import pandas as pd
import matplotlib
from pylab import title, figure, xlabel, ylabel, xticks, bar, legend, axis, savefig
from fpdf import FPDF
import matplotlib.pyplot as plt
import numpy as np
import os
from os import getcwd
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
from datetime import date
# -----------------------------------------------------------------------
import sqlite3
global curs
global conn
global Tarih
global Month

Month=[]
LastVer=500
harfler = ['ğ', 'ı', 'ö', 'ü', 'ş']
degistirilecekler = ['g', 'i', 'o', 'u', 's']
eslesmeler = str.maketrans("".join(harfler), "".join(degistirilecekler))
conn=sqlite3.connect('./Database/Tespit_Edilen_Veriler.db',timeout=1, check_same_thread=False)
curs=conn.cursor()
curs2=conn.cursor()
sorguVeri=("""CREATE TABLE IF NOT EXISTS Hata_Sonuclari(
                 Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                 Tarih TEXT NOT NULL UNIQUE,
                 Dok_No INTEGER NOT NULL,
                 Kalite_No INTEGER NOT NULL,
                 Hatanin_Geldiği_Metre INTEGER NOT NULL,
                 Bez_Eni INTEGER NOT NULL,
                 Hatanin_Duvar_Tarafından_Mesafesi INTEGER NOT NULL,
                 Hata_Eni INTEGER NOT NULL,
                 Hata_Boyutu INTEGER NOT NULL,
                 Hata_Alanı INTEGER NOT NULL,
                 Hata_Sınıfı TEXT NOT NULL,
                 Sonuc_Isım INTEGER NOT NULL)
                 """)
curs.execute(sorguVeri)
conn.commit()
Data = curs.fetchall()
class Data_Pre_Process_Lister:
    class CustomPDF(FPDF):
        def __init__(self, orientation = 'P', unit = 'mm', format='A4', Threshold_Tarih=None, Threshold_Tarih_Last=None, inf_pdf=None):
            FPDF.__init__(self, orientation, unit, format)
            self.Threshold_Tarih = Threshold_Tarih
            self.Threshold_Tarih_Last = Threshold_Tarih_Last
            self.inf_pdf = inf_pdf
            print(self.inf_pdf)
        def Line(self, HEIGHT, WIDTH):
            self.line(10, 10, 10, HEIGHT-10)
            self.line(HEIGHT-150, 10, WIDTH-63, HEIGHT-255)
            self.line(HEIGHT-245, 10, WIDTH-158, HEIGHT-255)
            self.line(HEIGHT-150, HEIGHT-270, WIDTH-10, HEIGHT-270)
            self.line(10, 10, WIDTH-10, 10)
            self.line(WIDTH-10, 10, 200, HEIGHT-10)
            self.line(10, HEIGHT-10, WIDTH-10, HEIGHT-10)
            self.line(10, HEIGHT-255, WIDTH-10, HEIGHT-255)
        def header(self):
            self.set_font('Arial', 'B', 15)
            self.cell(self.w / 2)
            self.ln(20)
            #Menderes Header
            self.image('./Icon/PDF/MenderesLogo.png', 15, 22, 33)
            self.set_font('Arial', 'B', 15)
            self.set_y(20)
            self.cell(63)
            self.cell(0, 5, 'Merserize Makinesinde   ', ln=1,link='C')
            self.set_y(27)
            self.cell(66)
            self.cell(0, 5, "Tespit Edilen Kumas", ln=1,link='C')
            self.set_y(34)
            self.cell(82)
            self.cell(0, 5, "Hatalari", ln=1,link='C')
            self.set_y(15)
            self.cell(140)
            self.ln(20)
            self.set_line_width(0.5)
            WIDTH=210
            HEIGHT=297
            self.Line(HEIGHT, WIDTH)
            self.set_y(15)
            self.cell(140)
            self.set_xy(WIDTH/5, HEIGHT/5)
        def table_details(self, row):
            # Tablo başlıkları
            self.set_font('Arial', 'B', 12)
            self.set_fill_color(240, 240, 240)
            self.set_text_color(0, 0, 0)
            self.set_x(28)
            self.cell(60, 5, f'Dok No:{row[2]}', 1, 0, 'C', True)
            quality = None
            if len(row[3]) > 8:
                quality = row[3][:8]
            else:
                quality = row[3]
            self.cell(60, 5, f'Kalite No:{quality}', 1, 1, 'C', True)

            self.set_x(28)
            self.set_fill_color(144, 144, 144)
            self.set_text_color(0, 0, 0)
            self.cell(60, 5, 'Hatanin Yatay Konumu(cm)', 1, 0, 'C', True, 'C')
            self.set_fill_color(240, 240, 240)
            self.set_fill_color(144, 144, 144)
            self.cell(60, 5, str(row[6]), 1, 1, 'C', True)

            self.set_x(28)
            self.set_fill_color(240, 240, 240)
            self.set_text_color(0, 0, 0)
            self.cell(60, 5, 'Hatanin Geldigi Metre(m)', 1, 0, 'C', True, 'C')
            self.set_fill_color(240, 240, 240)
            self.set_text_color(0, 0, 0)
            self.cell(60, 5, str(row[4]), 1, 1, 'C', True)

            self.set_x(28)
            self.set_fill_color(144, 144, 144)
            self.set_text_color(0, 0, 0)
            self.cell(60, 5, 'Hata Eni(mm)', 1, 0, 'C', True, 'C')
            self.set_fill_color(240, 240, 240)
            self.set_fill_color(144, 144, 144)
            self.cell(60, 5, str(row[7]), 1, 1, 'C', True)
            self.set_fill_color(240, 240, 240)
            self.set_text_color(0, 0, 0)
            self.set_x(28)
            self.cell(60, 5, 'Hata Boyu(mm)', 1, 0, 'C', True)
            self.set_fill_color(240, 240, 240)
            self.set_text_color(0, 0, 0)
            self.cell(60, 5, str(row[8]), 1, 1, 'C', True)
            self.set_fill_color(144, 144, 144)
            self.set_text_color(0, 0, 0)
            self.set_x(28)
            self.cell(60, 5, 'Hata Alani(mm2)', 1, 0, 'C', True)
            self.set_fill_color(240, 240, 240)
            self.set_fill_color(144, 144, 144)
            self.cell(60, 5, str(row[9]), 1, 1, 'C', True)
            self.set_fill_color(240, 240, 240)
            self.set_text_color(0, 0, 0)
            self.set_x(28)
            self.cell(60, 5, 'Hata Sinifi', 1, 0, 'C', True)
            self.set_fill_color(240, 240, 240)
            self.set_text_color(0, 0, 0)
            self.cell(60, 5, str(row[10]), 1, 1, 'C', True)
            self.set_fill_color(144, 144, 144)
            self.set_text_color(0, 0, 0)
            self.set_x(28)
            self.cell(60, 5, 'Hatanin Geldigi Tarih', 1, 0, 'C', True)
            self.set_fill_color(144, 144, 144)
            self.set_text_color(0, 0, 0)
            self.cell(60, 5, str(row[1]), 1, 1, 'C', True)
            self.set_text_color(0, 0, 0)
            # Hata görseli
            img_path = row[11]
            file_parts = img_path.split("/")
            file_parts[-2] = "images/cropped"
            new_file_path = "/".join(file_parts)
            try:
                self.image(new_file_path, 210 - 57, self.y - 40.5, 41, 41)
            except:
                self.set_draw_color(0, 0, 0)  # Çerçeve rengi
                self.rect(210 - 75, self.y - 25, 25, 25, 'D')
                self.set_fill_color(192, 192, 192)  # Dikdörtgen rengi
                self.rect(210 - 74.5, self.y - 24.5, 24, 24, 'F')
        def create_pdf_details(self):
            dok_no = 0
            leke_hatası = 0
            delik_hatası = 0
            limited_error = False
            # Tablodan verileri çekme
            if None == self.inf_pdf:
                curs.execute("SELECT * FROM Hata_Sonuclari WHERE Tarih BETWEEN ? AND ?", (self.Threshold_Tarih, self.Threshold_Tarih_Last))
                rows = curs.fetchall()
                if len(rows) > 200:
                    curs.execute("SELECT * FROM Hata_Sonuclari WHERE Tarih BETWEEN ? AND ? AND (Hata_Sınıfı = 'leke' OR Hata_Sınıfı = 'delik') ORDER BY RANDOM() LIMIT 200", (self.Threshold_Tarih, self.Threshold_Tarih_Last))
                    rows = curs.fetchall()
                    limited_error = True
                else:
                    limited_error = False

                # Tüm kayıtlar için tablo oluşturma
                if limited_error == False:
                    for i, row in enumerate(rows):
                        delik_hatası += 1 if row[10] == "delik" else 0
                        leke_hatası += 1 if row[10] == "leke" else 0
                        if row[2] != dok_no:
                            if i != 0:
                                self.cell(190, 10, txt=f"Toplam Delik: {delik_hatası}, Toplam Leke: {leke_hatası}", ln=1, align='C')
                                self.add_page()
                        if i % 4 == 0:
                            self.add_page()
                            delik_hatası = 0
                            leke_hatası = 0
                        # Tablo başlığı
                        self.set_font('Arial', 'B', 12)
                        self.ln()
                        # Tablo içeriği
                        self.table_details(row)
                        self.ln()
                        dok_no = row[2]
                else:
                    for i, row in enumerate(rows):
                        if i % 4 == 0:
                            self.add_page()
                        # Tablo başlığı
                        self.set_font('Arial', 'B', 12)
                        self.ln()
                        # Tablo içeriği
                        self.table_details(row)
                        self.ln()
            else:
                curs.execute("SELECT * FROM Hata_Sonuclari WHERE Tarih=? AND Dok_No=? AND Kalite_No=?",(self.inf_pdf[0], self.inf_pdf[1], self.inf_pdf[2]))
                rows = curs.fetchall()
                if len(rows) > 200:
                    curs.execute("SELECT * FROM Hata_Sonuclari WHERE Tarih=? AND Dok_No=? AND Kalite_No=? AND Hata_Sınıfı IN ('delik', 'leke') ORDER BY CASE WHEN Hata_Sınıfı = 'delik' THEN 0 ELSE 1 END, ROWID LIMIT 200 OFFSET 0", (self.inf_pdf[0], self.inf_pdf[1], self.inf_pdf[2]))
                    rows = curs.fetchall()
                    limited_error = True
                else:
                    limited_error = False

                # Tüm kayıtlar için tablo oluşturma
                if limited_error == False:
                    for i, row in enumerate(rows):
                        delik_hatası += 1 if row[10] == "delik" else 0
                        leke_hatası += 1 if row[10] == "leke" else 0
                        if row[2] != dok_no:
                            if i != 0:
                                self.cell(190, 10, txt=f"Toplam Delik: {delik_hatası}, Toplam Leke: {leke_hatası}", ln=1, align='C')
                                self.add_page()
                        if i % 4 == 0:
                            self.add_page()
                            delik_hatası = 0
                            leke_hatası = 0
                        # Tablo başlığı
                        self.set_font('Arial', 'B', 12)
                        self.ln()
                        # Tablo içeriği
                        self.table_details(row)
                        self.ln()
                        dok_no = row[2]
                else:
                    for i, row in enumerate(rows):
                        if i % 4 == 0:
                            self.add_page()
                        # Tablo başlığı
                        self.set_font('Arial', 'B', 12)
                        self.ln()
                        # Tablo içeriği
                        self.table_details(row)
                        self.ln()
        def footer(self):
            self.set_y(-10)
            self.set_font('Arial',size=12)
            page = 'Sayfa ' + str(self.page_no()) + '/{nb}'
            self.cell(0, 10, page, 0, 0, 'C')
        def meter_Bar(self, baslangic_tarihi, bitis_tarihi, hata_sinifi):
            WIDTH=210
            HEIGHT=297
            import itertools
            # Verileri sorgula
            query = """SELECT Dok_No, Kalite_No, Hatanin_Geldiği_Metre 
                    FROM Hata_Sonuclari 
                    WHERE Tarih BETWEEN ? AND ? AND Hata_Sınıfı = ?"""
            curs.execute(query, (baslangic_tarihi, bitis_tarihi, hata_sinifi))
            results = curs.fetchall()
            print("curs-fetchalladı")
            # Gruplama işlemi yap
            results.sort(key=lambda x: (x[0], x[1])) # İlk önce dok_no'ya göre sırala, ardından kalite_no'ya göre sırala
            groups = []
            for key, group in itertools.groupby(results, lambda x: (x[0], x[1])):
                groups.append((key, [row[2] for row in group]))
                print("key")

            # Grupları yazdır
            i=0
            for group in groups:
                print("groups")
                metres = np.array(group[1])
                mean = np.mean(metres)
                std_dev = np.std(metres)
                threshold = mean + 3 * std_dev  # Burada 3 kat standart sapma kullanarak aykırı değerleri belirliyoruz.

                filtered_metres = [metre for metre in metres if metre < threshold]
                if len(filtered_metres) == 0:
                    filtered_metres = [0]

                max_metre = max(filtered_metres)
                num_bars = int(max_metre / 250) + 1
                counts = [0] * num_bars

                for metre in filtered_metres:
                    bar_index = int(metre / 250)
                    counts[bar_index] += 1
                x_labels = [f"{i*250}-{(i+1)*250-1}" for i in range(num_bars)]
                plt.bar(x_labels, counts)
                plt.tick_params(axis='x', labelsize=8, rotation=90)

                plt.title(f"{hata_sinifi} için;Dok No: {group[0][0]}, Kalite No: {group[0][1]}")
                plt.xlabel("Hatanin Geldiği Metre Aralığı")
                plt.ylabel("Hata Sayısı")
                plt.savefig(f"./PDF/fig/{hata_sinifi}_Dok_No_{group[0][0]}_Kalite_No_{group[0][1]}.png")
                plt.cla()
                plt.clf()
                
                if hata_sinifi == "leke":
                    try:
                        self.set_xy(WIDTH/9, HEIGHT/7)
                        self.image(f"./PDF/fig/delik_Dok_No_{group[0][0]}_Kalite_No_{group[0][1]}.png", w = 170, h = 100, type = '', link = 'C')
                        self.image(f"./PDF/fig/{hata_sinifi}_Dok_No_{group[0][0]}_Kalite_No_{group[0][1]}.png", w = 170, h = 100, type = '', link = 'C')
                        self.add_page()
                    except:
                        pass
                
    def __init__(self, Threshold_Tarih, Threshold_Tarih_Last, inf_pdf):
        self.inf_pdf = inf_pdf
        self.out_path_main = ""
        self.Res_Tarih_Splited=[]
        self.Re_Tarih_Splited=[]
        self.Tarih="17.8.2022"
        self.Threshold_Tarih=Threshold_Tarih
        self.Threshold_Tarih_Last=Threshold_Tarih_Last
        self.Data = {
            'Hafta' : 7,
            'Tarih_Array' : [ [] , [] , [], [] ],
            'Tarih_Splited' : [],
            'Konum' : [ [] , [] , [], [] ],
            'Konum_Array' : [],
            'Hata_Türleri': ["delik","leke","kirik", "dikis", "iplik"],
            'Hata_Sayac' : [ [0] , [0] , [0] , [0] ],
            'Hata_Array' : [ [] , [] , [] , [] ],
            'Hata_Konum' : [ [], [], [], [] ],
            'Tarih_All':[]
                }
        curs.execute("SELECT * FROM Hata_Sonuclari")
        
    def positioning(self, Tarih):
        self.Tarih=Tarih
        for satirIndex, satirVeri in enumerate(curs):
            if self.Tarih == satirVeri[1]:
                if satirVeri[10] == self.Data['Hata_Türleri'][0]:
                    self.Data['Tarih_Array'][0].append(satirVeri[1])
                    self.Data['Hata_Array'][0].append(self.Data['Hata_Türleri'][0])    
                    self.Data['Hata_Konum'][0].append(satirIndex)
                    self.Data['Hata_Sayac'][0][0] = int(self.Data['Hata_Sayac'][0][0]+1)
                if satirVeri[10] == self.Data['Hata_Türleri'][1]:
                    self.Data['Tarih_Array'][1].append(satirVeri[1])
                    self.Data['Hata_Array'][1].append(self.Data['Hata_Türleri'][1])    
                    self.Data['Hata_Konum'][1].append(satirIndex)
                    self.Data['Hata_Sayac'][1][0] = int(self.Data['Hata_Sayac'][1][0]+1)
                if satirVeri[10] == self.Data['Hata_Türleri'][2]:
                    self.Data['Tarih_Array'][2].append(satirVeri[1])
                    self.Data['Hata_Array'][2].append(self.Data['Hata_Türleri'][2] + self.Data['Hata_Türleri'][3] + self.Data['Hata_Türleri'][4])
                    self.Data['Hata_Konum'][2].append(satirIndex)
                    self.Data['Hata_Sayac'][2][0] = int(self.Data['Hata_Sayac'][2][0]+1)
            elif self.Tarih=="All":
                self.Data['Tarih_All'].append(satirVeri[1])
        return self.Data
    
    def PDF_W(self):
        Res_Tarih_Splited=self.Res_Tarih_Splited
        Re_Tarih_Splited=self.Re_Tarih_Splited
        Tarih_Splited=Data_Pre_Process_Lister(self.Threshold_Tarih, self.Threshold_Tarih_Last, self.inf_pdf).positioning('All')['Tarih_Splited']
        Tarih_Array=Data_Pre_Process_Lister(self.Threshold_Tarih, self.Threshold_Tarih_Last, self.inf_pdf).positioning('All')['Tarih_All']
        Hafta=Data_Pre_Process_Lister(self.Threshold_Tarih, self.Threshold_Tarih_Last, self.inf_pdf).positioning('All')['Hafta']
        for item in Tarih_Array: 
            if item not in Res_Tarih_Splited:
                Res_Tarih_Splited.append(item) 
        Day_Threshold=int(self.Threshold_Tarih.split('.')[0])
        Month_Threshold=int(self.Threshold_Tarih.split('.')[1])
        Year_Threshold=int(self.Threshold_Tarih.split('.')[2])
        Day_Threshold_Last=int(self.Threshold_Tarih_Last.split('.')[0])
        Month_Threshold_Last=int(self.Threshold_Tarih_Last.split('.')[1])
        Year_Threshold_Last=int(self.Threshold_Tarih_Last.split('.')[2])
        
        for Thresh in range(len(Res_Tarih_Splited)):
            Now=date(int(Res_Tarih_Splited[Thresh].split('.')[2]), int(Res_Tarih_Splited[Thresh].split('.')[1]), int(Res_Tarih_Splited[Thresh].split('.')[0]))
            Low_Thresh=date(Year_Threshold, Month_Threshold, Day_Threshold)
            High_Thresh=date(Year_Threshold_Last, Month_Threshold_Last, Day_Threshold_Last)
            Low_Delta=Now-Low_Thresh
            High_Delta=High_Thresh-Now
            if int(Low_Delta.days)>=0 and abs(int(High_Delta.days))>=0:
                Re_Tarih_Splited.append(Res_Tarih_Splited[Thresh])
        self.Tarih=Re_Tarih_Splited[-1]
        Tarih_Splited=[Re_Tarih_Splited[x:x+Hafta] for x in range(0, len(Re_Tarih_Splited), Hafta)]
        
        def Week_Datas(Datas):
            Toplam_Delik=0
            Toplam_Leke=0
            Toplam_Yag=0
            Toplam_Iplik=0
            Toplam=[]
            
            for gün in range(0,len(Datas),1):
                L=Data_Pre_Process_Lister(self.Threshold_Tarih, self.Threshold_Tarih_Last, self.inf_pdf).positioning(str(Datas[gün]))['Hata_Sayac']
                Toplam_Delik= Toplam_Delik+L[0][0]
                Toplam_Leke= Toplam_Leke+L[1][0]
                Toplam_Yag= Toplam_Yag+L[2][0]
                Toplam_Iplik= Toplam_Iplik+L[3][0]
            Toplam.append(Toplam_Delik)
            Toplam.append(Toplam_Leke)
            Toplam.append(Toplam_Yag)
            Toplam.append(Toplam_Iplik)
            return Toplam
        
        for Week in range(len(Tarih_Splited)):
            Toplam=Week_Datas(Tarih_Splited[Week])
            Month.append(f'{Week+1}. Hafta')
            Month.append(Toplam)
        
        def Line(HEIGHT, WIDTH,pdf):
            pdf.line(10, 10, 10, HEIGHT-10)
            pdf.line(HEIGHT-150, 10, WIDTH-63, HEIGHT-255)
            pdf.line(HEIGHT-245, 10, WIDTH-158, HEIGHT-255)
            pdf.line(HEIGHT-150, HEIGHT-270, WIDTH-10, HEIGHT-270)
            pdf.line(10, 10, WIDTH-10, 10)
            pdf.line(WIDTH-10, 10, 200, HEIGHT-10)
            pdf.line(10, HEIGHT-10, WIDTH-10, HEIGHT-10)
            pdf.line(10, HEIGHT-255, WIDTH-10, HEIGHT-255)
    
        df = pd.DataFrame()
        df2 = pd.DataFrame()
        if len(Tarih_Splited)==1:
            df['Question'] = [f"{Tarih_Splited[0][0]}-{Tarih_Splited[0][-1]}"]
            df2['Question']=['1. Hafta']
            df['delik'] = [Month[1][0]]
            df['leke'] = [Month[1][1]]
            df['Diger'] = [Month[1][2]]
            d = [2.0]
            h= [1.5]
            
        elif len(Tarih_Splited)==2:
            df['Question'] = [f"{Tarih_Splited[0][0]}-{Tarih_Splited[0][-1]}", f"{Tarih_Splited[1][0]}-{Tarih_Splited[1][-1]}"]
            df2['Question']=['1. Hafta','2. Hafta']
            df['delik'] = [Month[1][0], Month[3][0]]
            df['leke'] = [Month[1][1], Month[3][1]]
            df['Diger'] = [Month[1][2], Month[3][2]]
            d = [2.0, 4.0]
            h= [1.5, 3.5]
        elif len(Tarih_Splited)==3:
            df['Question'] = [f"{Tarih_Splited[0][0]}-{Tarih_Splited[0][-1]}",
                               f"{Tarih_Splited[1][0]}-{Tarih_Splited[1][-1]}",
                               f"{Tarih_Splited[2][0]}-{Tarih_Splited[2][-1]}"
                             ]
            df2['Question']=['1. Hafta', '2. Hafta', '3. Hafta']
            df['delik'] = [Month[1][0], Month[3][0], Month[5][0]]
            df['leke'] = [Month[1][1], Month[3][1], Month[5][1]]
            df['Diger'] = [Month[1][2], Month[3][2], Month[5][2]]
            d = [2.0, 4.0, 6.0]
            h= [1.5, 3.5, 5.5]
        else:
            df['Question'] = [f"{Tarih_Splited[0][0]}-{Tarih_Splited[0][-1]}",
                              f"{Tarih_Splited[1][0]}-{Tarih_Splited[1][-1]}",
                              f"{Tarih_Splited[2][0]}-{Tarih_Splited[2][-1]}",
                              f"{Tarih_Splited[3][0]}-{Tarih_Splited[3][-1]}"
                             ]
            
            df2['Question']=['1. Hafta', '2. Hafta', '3. Hafta', '4. Hafta']
            df['delik'] = [Month[-7][0], Month[-5][0], Month[-3][0], Month[-1][0]]
            df['leke'] = [Month[-7][1], Month[-5][1], Month[-3][1], Month[-1][1]]
            df['Diger'] = [Month[-7][2], Month[-5][2], Month[-3][2], Month[-1][2]]
            d = [2.0, 4.0, 6.0, 8.0]
            h= [1.5, 3.5, 5.5, 7.5]
        title("Hata Barı", fontsize=15, fontname='Arial')
        xlabel('Tarih', fontsize=12, fontname='Arial')
        ylabel('Adet', fontsize=12, fontname='Arial')
        axis([0, 12, 0, LastVer])
        m = [x - 0.5 for x in d]
        y = [x - 0.5 for x in m]
        I = [x - 0.5 for x in y]
        xticks(d, df2['Question'])
        plt.bar(m, df['delik'], width=0.5, color="#521B1D", label="delik")
        plt.bar(d, df['leke'], width=0.5, color="#39521B", label="leke")
        plt.bar(y, df['Diger'], width=0.5, color="#1B5250", label="Diger")
        plt.legend()
        savefig('barchart.png')
        plt.cla()
        plt.clf()
        WIDTH=210
        HEIGHT=297
        pdf = self.CustomPDF(orientation = 'P', unit = 'mm', format='A4',Threshold_Tarih=self.Threshold_Tarih, Threshold_Tarih_Last=self.Threshold_Tarih_Last, inf_pdf=self.inf_pdf)
        pdf.alias_nb_pages()
        pdf.add_page()
        pdf.set_line_width(0.5)
        Line(HEIGHT, WIDTH,pdf)
        pdf.set_y(15)
        pdf.cell(140)
        pdf.cell(0, 5, f'Tarih: {Re_Tarih_Splited[-1]}', ln=1)
        pdf.set_font('Arial',size=12)
        pdf.set_xy(WIDTH/5, HEIGHT/5)
        pdf.cell(50, 10, 'Hafta', 1, 0, 'C')
        pdf.cell(40, 10, 'delik', 1, 0, 'C')
        pdf.cell(40, 10, 'leke', 1, 2, 'C')
        pdf.cell(-90)
        pdf.set_font('Arial',size=12)
        for i in range(0, len(df)):
            pdf.cell(50, 10, '%s' % (df['Question'].iloc[i]), 1, 0, 'C')
            pdf.cell(40, 10, '%s' % (str(df.delik.iloc[i])), 1, 0, 'C')
            pdf.cell(40, 10, '%s' % (str(df.leke.iloc[i])), 1, 2, 'C')
            pdf.cell(-90)
        pdf.set_y(110)
        pdf.cell(30,10,link = 'C')
        pdf.image('barchart.png', w = 136, h = 80, type = '', link = 'C')
        pdf.set_y(190)
        pdf.cell(30,10,link = 'C')
        pdf.set_font('Arial', 'B', 15)
        pdf.cell(0, 15, f"{str(Re_Tarih_Splited[0])}-{str(Re_Tarih_Splited[-1])}'leri arasinda hata tespit turleri;", ln=1, align="")
        pdf.set_x(-180)
        pdf.set_font('Arial',size=12)
        if len(Tarih_Splited)==1:
            print(Tarih_Splited)
            pdf.cell(0, 10, f"{Tarih_Splited[0][0]}-{Tarih_Splited[0][-1]}'leri arasinda tespit edilen Delik ve Leke sayisi: {Month[1][0]}-{Month[1][1]} (Adet)",ln=0.5, align="")
        elif len(Tarih_Splited)==2:
            pdf.cell(0, 10, f"{Tarih_Splited[0][0]}-{Tarih_Splited[0][-1]}'leri arasinda tespit edilen Delik ve Leke sayisi: {Month[1][0]}-{Month[1][1]} (Adet)",ln=0.5, align="")
            pdf.cell(0, 10, f"{Tarih_Splited[1][0]}-{Tarih_Splited[1][-1]}'leri arasinda tespit edilen Delik ve Leke sayisi: {Month[3][0]}-{Month[3][1]} (Adet)",ln=0.5, align="")
        elif len(Tarih_Splited)==3:
            pdf.cell(0, 10, f"{Tarih_Splited[0][0]}-{Tarih_Splited[0][-1]}'leri arasinda tespit edilen Delik ve Leke sayisi: {Month[1][0]}-{Month[1][1]} (Adet)",ln=0.5, align="")
            pdf.cell(0, 10, f"{Tarih_Splited[1][0]}-{Tarih_Splited[1][-1]}'leri arasinda tespit edilen Delik ve Leke sayisi: {Month[3][0]}-{Month[3][1]} (Adet)",ln=0.5, align="")
            pdf.cell(0, 10, f"{Tarih_Splited[2][0]}-{Tarih_Splited[2][-1]}'leri arasinda tespit edilen Delik ve Leke sayisi: {Month[5][0]}-{Month[5][1]} (Adet)",ln=0.5, align="")
        else:
            pdf.cell(0, 10, f"{Tarih_Splited[-4][0]}-{Tarih_Splited[-4][-1]}'leri arasinda tespit edilen Delik ve Leke sayisi: {Month[-7][0]}-{Month[-7][1]} (Adet)",ln=0.5, align="")
            pdf.cell(0, 10, f"{Tarih_Splited[-3][0]}-{Tarih_Splited[-3][-1]}'leri arasinda tespit edilen Delik ve Leke sayisi: {Month[-5][0]}-{Month[-5][1]} (Adet)",ln=0.5, align="")
            pdf.cell(0, 10, f"{Tarih_Splited[-2][0]}-{Tarih_Splited[-2][-1]}'leri arasinda tespit edilen Delik ve Leke sayisi: {Month[-3][0]}-{Month[-3][1]} (Adet)",ln=0.5, align="")
            pdf.cell(0, 10, f"{Tarih_Splited[-1][0]}-{Tarih_Splited[-1][-1]}'leri arasinda tespit edilen Delik ve Leke sayisi: {Month[-1][0]}-{Month[-1][1]} (Adet)",ln=0.5, align="")
        if None == self.inf_pdf:
            baslangic_id, bitis_id = curs.execute(f"SELECT MIN(Id), MAX(Id) FROM Hata_Sonuclari WHERE Tarih BETWEEN '{self.Threshold_Tarih}' AND '{self.Threshold_Tarih_Last}'").fetchone()
            datas = curs.execute(f'''SELECT Tarih, Dok_No, Kalite_No, 
                    SUM(CASE WHEN Hata_Sınıfı = 'leke' THEN 1 ELSE 0 END) AS leke, 
                    SUM(CASE WHEN Hata_Sınıfı = 'delik' THEN 1 ELSE 0 END) AS delik
                    FROM Hata_Sonuclari
                    WHERE Id BETWEEN {baslangic_id} AND {bitis_id}
                    GROUP BY Tarih, Dok_No, Kalite_No
                    ORDER BY Id ASC''').fetchall()
        else:
            baslangic_id, bitis_id = curs.execute(f"SELECT MIN(Id), MAX(Id) FROM Hata_Sonuclari WHERE Tarih=? AND Dok_No=? AND Kalite_No=?",(self.inf_pdf[0], self.inf_pdf[1], self.inf_pdf[2])).fetchone()
            datas = curs.execute(f'''SELECT Tarih, Dok_No, Kalite_No, 
                    SUM(CASE WHEN Hata_Sınıfı = 'leke' THEN 1 ELSE 0 END) AS leke, 
                    SUM(CASE WHEN Hata_Sınıfı = 'delik' THEN 1 ELSE 0 END) AS delik
                    FROM Hata_Sonuclari
                    WHERE Id BETWEEN {baslangic_id} AND {bitis_id}
                    GROUP BY Tarih, Dok_No, Kalite_No
                    ORDER BY Id ASC''').fetchall()
        pdf.add_page()
        pdf.set_line_width(0.5)
        Line(HEIGHT, WIDTH, pdf)
        pdf.set_y(15)
        pdf.cell(140)
        pdf.cell(0, 5, f'Tarih: {Res_Tarih_Splited[-1]}', ln=1)
        pdf.set_font('Arial',size=12)
        pdf.set_xy(WIDTH/6, HEIGHT/5)
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(30, 10, 'Tarih', 1)
        pdf.cell(30, 10, 'Dok No', 1)
        pdf.cell(30, 10, 'Kalite No', 1)
        pdf.cell(30, 10, 'Delik Sayisi', 1)
        pdf.cell(30, 10, 'Leke Sayisi', 1)
        pdf.ln()
        # Tablo verileri
        pdf.set_font('Arial', '', 12)
        tarih_listesi = []
        delik_listesi = []
        leke_listesi = []
        for row in datas:
            tarih, dok_no, kalite_no, delik_sayisi, leke_sayisi = row
            if len(kalite_no) > 8:
                quality = kalite_no[:8]
            else:
                quality = kalite_no
            pdf.set_x(WIDTH/6)
            pdf.cell(30, 10, str(tarih), 1)
            pdf.cell(30, 10, str(dok_no), 1)
            pdf.cell(30, 10, str(quality).translate(eslesmeler), 1)
            pdf.cell(30, 10, str(leke_sayisi), 1)
            pdf.cell(30, 10, str(delik_sayisi), 1)
            tarih_listesi.append(str(tarih))
            delik_listesi.append(int(delik_sayisi))
            leke_listesi.append(int(leke_sayisi))
            pdf.ln()
        pdf.add_page()
        pdf.set_xy(WIDTH/9, HEIGHT/7)
        tarih_listesi_bar = [tarih.split(".")[0] + "." + tarih.split(".")[1] for tarih in tarih_listesi]
        plt.title("Tarihe Göre Delik Hatası Dağılım Grafiği")
        plt.bar(tarih_listesi_bar, leke_listesi)
        plt.tick_params(axis='x', labelsize=8, rotation=90)
        plt.ylabel('Leke Sayısı')
        plt.savefig('lekeler.png')
        pdf.image('lekeler.png', w = 170, h = 100, type = '', link = 'C')
        plt.clf()
        plt.cla()
        pdf.set_xy(WIDTH/9, HEIGHT/2+10)
        plt.title("Tarihe Göre Leke Hatası Dağılım Grafiği")
        plt.bar(tarih_listesi_bar, delik_listesi)
        plt.tick_params(axis='x', labelsize=8, rotation=90)
        plt.ylabel('Delik Sayısı')
        plt.savefig('delikler.png')
        pdf.image('delikler.png', w = 170, h = 100, type = '', link = 'C')
        plt.clf()
        plt.cla()
        pdf.add_page()
        pdf.meter_Bar(self.Threshold_Tarih, self.Threshold_Tarih_Last, "delik")
        pdf.meter_Bar(self.Threshold_Tarih, self.Threshold_Tarih_Last, "leke")

        pdf.create_pdf_details()
        main_path = getcwd()
        main_path = main_path.replace('\\' , "/")
        main_path = main_path +'/' + "PDF" + "/" + str(Re_Tarih_Splited[0]) +str(Re_Tarih_Splited[-1]) + '-aylık-rapor.pdf'
        self.out_path_main = main_path
        print(self.out_path_main)
        pdf.output(main_path, 'F')
        os.system(main_path)