import pandas as pd
import matplotlib
from pylab import title, figure, xlabel, ylabel, xticks, bar, legend, axis, savefig
from fpdf import FPDF
import matplotlib.pyplot as plt
import numpy as np
import os
from os import getcwd

os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
# -----------------------------------------------------------------------
import sqlite3
global curs
global conn
global Tarih
global Month

Month=[]
LastVer=500
conn=sqlite3.connect('./Database/Tespit_Edilen_Veriler.db',timeout=1, check_same_thread=False)
curs=conn.cursor()
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
sorguTablo = '''SELECT Tarih, Dok_No, Kalite_No, 
                SUM(CASE WHEN Hata_Sınıfı = 'leke' THEN 1 ELSE 0 END) AS leke, 
                SUM(CASE WHEN Hata_Sınıfı = 'delik' THEN 1 ELSE 0 END) AS delik
                FROM Hata_Sonuclari
                GROUP BY Tarih, Dok_No, Kalite_No
                ORDER BY Id ASC'''
datas = curs.execute(sorguTablo).fetchall()
harfler = ['ğ', 'ı', 'ö', 'ü', 'ş']
degistirilecekler = ['g', 'i', 'o', 'u', 's']
eslesmeler = str.maketrans("".join(harfler), "".join(degistirilecekler))
curs.execute(sorguVeri)
conn.commit()
Data = curs.fetchall()

class Data_Pre_Process:
    class CustomPDF(FPDF):
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
            # Menderes
            self.image('./Icon/PDF/MenderesLogo.png', 15, 22, 33)
            self.set_font('Arial', 'B', 15)
            self.set_y(20)
            self.cell(63)
            self.cell(0, 5, 'Düz kasar 132 Makinesinde   ', ln=1,link='C')
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
            
        def footer(self):
            self.set_y(-10)
            self.set_font('Arial',size=12)
            page = 'Sayfa ' + str(self.page_no()) + '/{nb}'
            self.cell(0, 10, page, 0, 0, 'C')  
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
            self.cell(60, 5, 'Hata Eni', 1, 0, 'C', True, 'C')
            self.set_fill_color(240, 240, 240)
            self.set_fill_color(144, 144, 144)
            self.cell(60, 5, str(row[7]), 1, 1, 'C', True)
            self.set_fill_color(240, 240, 240)
            self.set_text_color(0, 0, 0)
            self.set_x(28)
            self.cell(60, 5, 'Hata Boyu', 1, 0, 'C', True)
            self.set_fill_color(240, 240, 240)
            self.set_text_color(0, 0, 0)
            self.cell(60, 5, str(row[8]), 1, 1, 'C', True)
            self.set_fill_color(144, 144, 144)
            self.set_text_color(0, 0, 0)
            self.set_x(28)
            self.cell(60, 5, 'Hata Alani', 1, 0, 'C', True)
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
            self.cell(60, 5, 'Tarih', 1, 0, 'C', True)
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
                self.image(new_file_path, 210 - 57, self.y - 25.5, 26, 26)
            except:
                self.set_draw_color(0, 0, 0)  # Çerçeve rengi
                self.rect(210 - 75, self.y - 25, 25, 25, 'D')
                self.set_fill_color(192, 192, 192)  # Dikdörtgen rengi
                self.rect(210 - 74.5, self.y - 24.5, 24, 24, 'F')
        def create_pdf_details(self):
            dok_no = 0
            leke_hatası = 0
            delik_hatası = 0
            # Tablodan verileri çekme
            curs.execute("SELECT * FROM Hata_Sonuclari ORDER BY Id")
            rows = curs.fetchall()
            # Tüm kayıtlar için tablo oluşturma
            for i, row in enumerate(rows):
                delik_hatası += 1 if row[10] == "delik" else 0
                leke_hatası += 1 if row[10] == "leke" else 0
                if row[2] != dok_no:
                    if i != 0:
                        self.cell(190, 10, txt=f"Toplam Delik: {delik_hatası}, Toplam Leke: {leke_hatası}", ln=1, align='C')
                        self.add_page()
                if i % 5 == 0:
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
    def __init__(self):
        self.Res_Tarih_Splited=[]
        self.Tarih="18.8.2022"
        self.Data = {
            'Hafta' : 7,
            'Tarih_Array' : [[], [], [], []],
            'Tarih_Splited' : [],
            'Konum' : [[], [], [], []],
            'Konum_Array' : [],
            'Hata_Türleri': ["delik","leke","kirik", "dikis", "iplik"],
            'Hata_Sayac' : [[0], [0], [0], [0]],
            'Hata_Array' : [[] , [] , [], []],
            'Hata_Konum' : [[], [], [], []],
            'Tarih_All':[]
                }
        

    def positioning(self, Tarih):
        self.Tarih=Tarih
        conn=sqlite3.connect('./Database/Tespit_Edilen_Veriler.db',timeout=1, check_same_thread=False)
        curs=conn.cursor()
        curs.execute("SELECT * FROM Hata_Sonuclari")
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
        Tarih_Splited=Data_Pre_Process().positioning("All")['Tarih_Splited']
        Tarih_Array=Data_Pre_Process().positioning("All")['Tarih_All']
        Hafta=Data_Pre_Process().positioning("All")['Hafta']
        for item in Tarih_Array: 
            if item not in Res_Tarih_Splited: 
                Res_Tarih_Splited.append(item) 
        self.Tarih=Res_Tarih_Splited[-1]
        Tarih_Splited=[Res_Tarih_Splited[x:x+Hafta] for x in range(0, len(Res_Tarih_Splited), Hafta)]
        def Week_Datas(Datas):
            Toplam_Delik=0
            Toplam_Leke=0
            Toplam_Diger=0
            Toplam=[]
            for gün in range(0,len(Datas),1):
                L=Data_Pre_Process().positioning(str(Datas[gün]))['Hata_Sayac']
                Toplam_Delik= Toplam_Delik+L[0][0]
                Toplam_Leke= Toplam_Leke+L[1][0]
                Toplam_Diger= Toplam_Diger + L[2][0] 
            Toplam.append(Toplam_Delik)
            Toplam.append(Toplam_Leke)
            Toplam.append(Toplam_Diger)
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
            df['Question'] = [f"{Tarih_Splited[0][0]}-{Tarih_Splited[0][-1]}",
                               f"{Tarih_Splited[1][0]}-{Tarih_Splited[1][-1]}"
                             ]
            df2['Question']=['1. Hafta','2. Hafta']
            df['delik'] = [Month[1][0], Month[3][0]]
            df['leke'] = [Month[1][1], Month[3][1]]
            df['Diger'] = [Month[1][2], Month[3][2]]
            d = [2.0, 4.0]
            h= [1.5, 3.5]
            print("Er *")
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
            df['Question'] = [f"{Tarih_Splited[-4][0]}-{Tarih_Splited[-4][-1]}",
                              f"{Tarih_Splited[-3][0]}-{Tarih_Splited[-3][-1]}",
                              f"{Tarih_Splited[-2][0]}-{Tarih_Splited[-2][-1]}",
                              f"{Tarih_Splited[-1][0]}-{Tarih_Splited[-1][-1]}"
                             ]
            df2['Question']=['1. Hafta', '2. Hafta', '3. Hafta', '4. Hafta']
            df['delik'] = [Month[-7][0], Month[-5][0], Month[-3][0], Month[-1][0]]
            df['leke'] = [Month[-7][1], Month[-5][1], Month[-3][1], Month[-1][1]]
            df['Diger'] = [Month[-7][2], Month[-5][2], Month[-3][2], Month[-1][2]]
            d = [2.0, 5.0, 8.0, 11.0]
            h= [1.5, 3.5, 5.5, 7.5]
        title("Hata Barı", fontsize=15, fontname='Arial')
        xlabel('Tarih', fontsize=12, fontname='Arial')
        ylabel('Adet', fontsize=12, fontname='Arial')
        axis([0, 16, 0, LastVer])
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
        pdf = self.CustomPDF(orientation = 'P', unit = 'mm', format='A4')
        pdf.alias_nb_pages()
        pdf.add_page()
        pdf.set_line_width(0.5)
        Line(HEIGHT, WIDTH,pdf)
        pdf.set_y(15)
        pdf.cell(140)
        pdf.cell(0, 5, f'Tarih: {Res_Tarih_Splited[-1]}', ln=1)
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
        pdf.cell(0, 15, f"{str(Res_Tarih_Splited[0])}-{str(Res_Tarih_Splited[-1])}'leri arasinda hata tespit turleri;", ln=1, align="")
        pdf.set_x(-180)
        pdf.set_font('Arial',size=12)
        if len(Tarih_Splited)==1:
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
        pdf.cell(30, 10, 'Leke Sayisi', 1)
        pdf.cell(30, 10, 'Delik Sayisi', 1)
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
            pdf.cell(30, 10, str(delik_sayisi), 1)
            pdf.cell(30, 10, str(leke_sayisi), 1)
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
        main_path = getcwd()
        main_path = main_path.replace('\\' , "/")
        main_path = main_path +'/' + "PDF" + "/" + str(self.Tarih) + '-aylık-rapor.pdf'
        print(main_path)
        # pdf.create_pdf_details()

        conn.close()
        pdf.output(main_path, 'F')
        os.system(main_path)
        