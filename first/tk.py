from tkinter import *
import tkinter as tk

import requests
from bs4 import BeautifulSoup

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.menubar = tk.Menu(self)
        self.config(menu=self.menubar)

    def getdata(url):
	    r = requests.get(url)
	    return r.text


    def airinfo():
	    htmldata = getdata("https://weather.com/zh-TW/forecast/air-quality/l/6b221b26e046a442e03dc46fbe91d5874c6461afde61187dd4126bddeea1e2aa")
	    soup = BeautifulSoup(htmldata, 'html.parser')
	    res_data = soup.find(class_="DonutChart--innerValue--3_iFF AirQuality--extendedDialText--1kqIb").text
	air_data = soup.find_all(class_="DonutChart--innerValue--3_iFF AirQuality--pollutantDialText--2Q5Oh")
	air_data=[data.text for data in air_data]
	

	ar.set(res_data)
	pm.set(air_data[0]) 
	co.set(air_data[1])
	no2.set(air_data[2])
	o3.set(air_data[3])
	pml.set(air_data[4])
	so2.set(air_data[5])

	res = int(res_data)
	if res <= 50:
		remark = "良好" #Good
		impact = "空氣品質為良好，污染程度低或無污染。"#Minimal impact
	elif res <= 100 and res > 51:
		remark = "普通"#Satisfactory
		impact = "空氣品質普通；但對非常少數之極敏感族群產生輕微影響。"#Minor breathing discomfort to sensitive people
	elif res <= 150 and res > 101:
		remark = "對敏感族群不健康"#Unhealthy for Sensitive Groups
		impact = "空氣污染物可能會對敏感族群的健康造成影響，但是對一般大眾的影響不明顯。"
	elif res <= 200 and res >= 151:
		remark = "對所有族群不健康"#Unhealthy
		impact = "對所有人的健康開始產生影響，對於敏感族群可能產生較嚴重的健康影響"
	elif res <= 400 and res >= 201:
		remark = "非常不健康"#Very Poor
		impact = "健康警報：所有人都可能產生較嚴重的健康影響。"
	elif res <= 500 and res >= 401:
		remark = "危害"#Severe
		impact = "健康威脅達到緊急，所有人都可能受到影響。"
	res_remark.set(remark)
	res_imp.set(impact)


def main():
    window = Window()
    window.title("空氣品質")
    window.mainloop()

if __name__ == "__main__":
    main()