from tkinter import *
import requests
from bs4 import BeautifulSoup


class AirQualityApp():
    def __init__(self, master):
        self.master = master
        master.configure(bg='light grey')
        self.air_data = StringVar()
        self.ar = StringVar()
        self.o3 = StringVar()
        self.no2 = StringVar()
        self.so2 = StringVar()
        self.pm = StringVar()
        self.pml = StringVar()
        self.co = StringVar()
        self.res_remark = StringVar()
        self.res_imp = StringVar()

        # Creating label for each information name using widget Label
        Label(self.master, text="空氣品質：", bg="light grey").grid(row=0, sticky=W)
        Label(self.master, text="O3 (μg/m3) 臭氧：", bg="light grey").grid(row=4, sticky=W)
        Label(self.master, text="NO2 (μg/m3) 二氧化氮：", bg="light grey").grid(row=3, sticky=W)
        Label(self.master, text="SO2 (μg/m3) 二氧化硫：", bg="light grey").grid(row=6, sticky=W)
        Label(self.master, text="PM2.5 (μg/m3) 懸浮微粒<2.5微米：", bg="light grey").grid(row=1, sticky=W)
        Label(self.master, text="PM10 (μg/m3) 懸浮微粒<10微米：", bg="light grey").grid(row=5, sticky=W)
        Label(self.master, text="CO (μg/m3)一氧化碳：", bg="light grey").grid(row=2, sticky=W)
        Label(self.master, text="對健康影響與活動建議：", bg="light grey").grid(row=7, sticky=W)
        Label(self.master, text="人體健康影響：", bg="light grey").grid(row=8, sticky=W)

        # Creating label for class variable name using widget Entry
        Label(self.master, text="", textvariable=self.ar, bg="light grey").grid(row=0, column=1, sticky=W)
        Label(self.master, text="", textvariable=self.pm, bg="light grey").grid(row=1, column=1, sticky=W)
        Label(self.master, text="", textvariable=self.co, bg="light grey").grid(row=2, column=1, sticky=W)
        Label(self.master, text="", textvariable=self.no2, bg="light grey").grid(row=3, column=1, sticky=W)
        Label(self.master, text="", textvariable=self.o3, bg="light grey").grid(row=4, column=1, sticky=W)
        Label(self.master, text="", textvariable=self.pml, bg="light grey").grid(row=5, column=1, sticky=W)
        Label(self.master, text="", textvariable=self.so2, bg="light grey").grid(row=6, column=1, sticky=W)
        Label(self.master, text="", textvariable=self.res_remark, bg="light grey").grid(row=7, column=1, sticky=W)
        Label(self.master, text="", textvariable=self.res_imp, bg="light grey").grid(row=8, column=1, sticky=W)
    

