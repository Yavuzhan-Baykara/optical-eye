import pandas as pd
import matplotlib
from pylab import title, figure, xlabel, ylabel, xticks, bar, legend, axis, savefig
from fpdf import FPDF
import matplotlib.pyplot as plt
import numpy as np
import os

os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

# -----------------------------------------------------------------------
import sqlite3
global curs
global conn
global Tarih
global Month



Month=[]
LastVer=40

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
                 
curs.execute(sorguVeri)
conn.commit()
Data = curs.fetchall()



        

class Data_Pre_Process:
    class CustomPDF(FPDF):
        def header(self):
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
        def footer(self):
            self.set_y(-10)
            self.set_font('Arial',size=12)
            page = 'Sayfa ' + str(self.page_no()) + '/{nb}'
            self.cell(0, 10, page, 0, 0, 'C')  
            
    def __init__(self):
        self.Res_Tarih_Splited=[]
        self.Tarih="18.8.2022"
        self.Data = {
            'Hafta' : 7,
            'Tarih_Array' : [ [] , [] , [], [] ],
            'Tarih_Splited' : [],
            'Konum' : [ [] , [] , [], [] ],
            'Konum_Array' : [],
            'Hata_Türleri': ["Delik","Leke","Yag","Iplik"],
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
                    self.Data['Hata_Array'][2].append(self.Data['Hata_Türleri'][2])    
                    self.Data['Hata_Konum'][2].append(satirIndex)
                    self.Data['Hata_Sayac'][2][0] = int(self.Data['Hata_Sayac'][2][0]+1)
                    
                if satirVeri[10] == self.Data['Hata_Türleri'][3]:
                    self.Data['Tarih_Array'][3].append(satirVeri[1])
                    self.Data['Hata_Array'][3].append(self.Data['Hata_Türleri'][3])    
                    self.Data['Hata_Konum'][3].append(satirIndex)
                    self.Data['Hata_Sayac'][3][0] = int(self.Data['Hata_Sayac'][3][0]+1)
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
        print(Tarih_Splited)
        def Week_Datas(Datas):
            Toplam_Delik=0
            Toplam_Leke=0
            Toplam_Yag=0
            Toplam_Iplik=0
            Toplam=[]
            for gün in range(0,len(Datas),1):
                L=Data_Pre_Process().positioning(str(Datas[gün]))['Hata_Sayac']
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
            df['Question'] = [f"{Tarih_Splited[0][0]}-{Tarih_Splited[0][-1]}"
                             ]
            df2['Question']=['1. Hafta']
            
            df['Delik'] = [Month[1][0]]
            df['Leke'] = [Month[1][1]]
            df['Yag'] = [Month[1][2]]
            df['Iplik'] = [Month[1][3]]
            d = [2.0]
            h= [1.5]
            
        elif len(Tarih_Splited)==2:
            df['Question'] = [f"{Tarih_Splited[0][0]}-{Tarih_Splited[0][-1]}",
                               f"{Tarih_Splited[1][0]}-{Tarih_Splited[1][-1]}"
                             ]
            df2['Question']=['1. Hafta','2. Hafta']
            df['Delik'] = [Month[1][0], Month[3][0]]
            df['Leke'] = [Month[1][1], Month[3][1]]
            df['Yag'] = [Month[1][2], Month[3][2]]
            df['Iplik'] = [Month[1][3], Month[3][3]]
            d = [2.0, 4.0]
            h= [1.5, 3.5]
            print("Er *")
        elif len(Tarih_Splited)==3:
            df['Question'] = [f"{Tarih_Splited[0][0]}-{Tarih_Splited[0][-1]}",
                               f"{Tarih_Splited[1][0]}-{Tarih_Splited[1][-1]}",
                               f"{Tarih_Splited[2][0]}-{Tarih_Splited[2][-1]}"
                             ]
            df2['Question']=['1. Hafta', '2. Hafta', '3. Hafta']
            df['Delik'] = [Month[1][0], Month[3][0], Month[5][0]]
            df['Leke'] = [Month[1][1], Month[3][1], Month[5][1]]
            df['Yag'] = [Month[1][2], Month[3][2], Month[5][2]]
            df['Iplik'] = [Month[1][3], Month[3][3], Month[5][3]]
            d = [2.0, 4.0, 6.0]
            h= [1.5, 3.5, 5.5]
        elif len(Tarih_Splited)==4:
            df['Question'] = [f"{Tarih_Splited[0][0]}-{Tarih_Splited[0][-1]}",
                              f"{Tarih_Splited[1][0]}-{Tarih_Splited[1][-1]}",
                              f"{Tarih_Splited[2][0]}-{Tarih_Splited[2][-1]}",
                              f"{Tarih_Splited[3][0]}-{Tarih_Splited[3][-1]}"
                             ]
            
            df2['Question']=['1. Hafta', '2. Hafta', '3. Hafta', '4. Hafta']
            df['Delik'] = [Month[1][0], Month[3][0], Month[5][0], Month[7][0]]
            df['Leke'] = [Month[1][1], Month[3][1], Month[5][1], Month[7][1]]
            df['Yag'] = [Month[1][2], Month[3][2], Month[5][2], Month[7][2]]
            df['Iplik'] = [Month[1][3], Month[3][3], Month[5][3], Month[7][3]]
            d = [2.0, 4.0, 6.0, 8.0]
            h= [1.5, 3.5, 5.5, 7.5]
        
        listx=df.loc[:,'Delik'].tolist()
        listy=df.loc[:,'Leke'].tolist()
        
        
        title("Hata Barı", fontsize=15, fontname='Arial')
        xlabel('Tarih', fontsize=12, fontname='Arial')
        ylabel('Adet', fontsize=12, fontname='Arial')
        axis([0, 12, 0, LastVer])
        
        m = [x - 0.5 for x in d]
        
        y = [x - 0.5 for x in m]
        
        I = [x - 0.5 for x in y]
        
        
        xticks(d, df2['Question'])
        
        # plt.plot(h, listx, label='Delik')
        # plt.plot(d, listy, '-r', label='Leke')
        
        plt.bar(m, df['Delik'], width=0.5, color="#521B1D", label="Delik")
        plt.bar(d, df['Leke'], width=0.5, color="#39521B", label="Leke")
        plt.bar(y, df['Yag'], width=0.5, color="#1B5250", label="Yag")
        plt.bar(I, df['Iplik'], width=0.5, color="#341B52", label="Iplik")
        
        
        plt.legend()
        
        savefig('barchart.png')
        
        plt.cla()
        
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
        pdf.cell(40, 10, 'Delik', 1, 0, 'C')
        pdf.cell(40, 10, 'Leke', 1, 2, 'C')
        pdf.cell(-90)
        pdf.set_font('Arial',size=12)
        
        for i in range(0, len(df)):
            pdf.cell(50, 10, '%s' % (df['Question'].iloc[i]), 1, 0, 'C')
            pdf.cell(40, 10, '%s' % (str(df.Delik.iloc[i])), 1, 0, 'C')
            pdf.cell(40, 10, '%s' % (str(df.Leke.iloc[i])), 1, 2, 'C')
            pdf.cell(-90)
        
        
        pdf.set_y(100)
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
        if len(Tarih_Splited)==2:
            pdf.cell(0, 10, f"{Tarih_Splited[0][0]}-{Tarih_Splited[0][-1]}'leri arasinda tespit edilen Delik ve Leke sayisi: {Month[1][0]}-{Month[1][1]} (Adet)",ln=0.5, align="")
            pdf.cell(0, 10, f"{Tarih_Splited[1][0]}-{Tarih_Splited[1][-1]}'leri arasinda tespit edilen Delik ve Leke sayisi: {Month[3][0]}-{Month[3][1]} (Adet)",ln=0.5, align="")
        if len(Tarih_Splited)==3:
            pdf.cell(0, 10, f"{Tarih_Splited[0][0]}-{Tarih_Splited[0][-1]}'leri arasinda tespit edilen Delik ve Leke sayisi: {Month[1][0]}-{Month[1][1]} (Adet)",ln=0.5, align="")
            pdf.cell(0, 10, f"{Tarih_Splited[1][0]}-{Tarih_Splited[1][-1]}'leri arasinda tespit edilen Delik ve Leke sayisi: {Month[3][0]}-{Month[3][1]} (Adet)",ln=0.5, align="")
            pdf.cell(0, 10, f"{Tarih_Splited[2][0]}-{Tarih_Splited[2][-1]}'leri arasinda tespit edilen Delik ve Leke sayisi: {Month[5][0]}-{Month[5][1]} (Adet)",ln=0.5, align="")
        if len(Tarih_Splited)==4:
            pdf.cell(0, 10, f"{Tarih_Splited[0][0]}-{Tarih_Splited[0][-1]}'leri arasinda tespit edilen Delik ve Leke sayisi: {Month[1][0]}-{Month[1][1]} (Adet)",ln=0.5, align="")
            pdf.cell(0, 10, f"{Tarih_Splited[1][0]}-{Tarih_Splited[1][-1]}'leri arasinda tespit edilen Delik ve Leke sayisi: {Month[3][0]}-{Month[3][1]} (Adet)",ln=0.5, align="")
            pdf.cell(0, 10, f"{Tarih_Splited[2][0]}-{Tarih_Splited[2][-1]}'leri arasinda tespit edilen Delik ve Leke sayisi: {Month[5][0]}-{Month[5][1]} (Adet)",ln=0.5, align="")
            pdf.cell(0, 10, f"{Tarih_Splited[3][0]}-{Tarih_Splited[3][-1]}'leri arasinda tespit edilen Delik ve Leke sayisi: {Month[7][0]}-{Month[7][1]} (Adet)",ln=0.5, align="")

        
        pdf.output('test2.pdf', 'F')
        os.system('test2.pdf')
        
        
        

        
