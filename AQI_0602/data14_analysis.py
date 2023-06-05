# data14_analysis.py
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

def tem_curve(data):
  """溫度曲線繪製"""
  date = list(data['日期'])
  tem_low = list(data['最低氣溫'])
  tem_high = list(data['最高氣溫'])
  for i in range(0,14):
    if math.isnan(tem_low[i]) == True:
      tem_low[i] = tem_low[i-1]
    if math.isnan(tem_high[i]) == True:
      tem_high[i] = tem_high[i-1]

  tem_high_ave = sum(tem_high)/14     # 求平均高溫 
  tem_low_ave = sum(tem_low)/14     # 求平均低溫 
  
  tem_max = max(tem_high)    
  tem_max_date = tem_high.index(tem_max)   # 求最高溫度
  tem_min = min(tem_low)
  tem_min_date = tem_low.index(tem_min)   # 求最低溫度

  x = range(1,15)
  plt.figure(1)
  plt.plot(x,tem_high,color='red',label='高溫')    # 畫出高溫度曲線
  plt.scatter(x,tem_high,color='red')     # 點出每個時刻的溫度點
  plt.plot(x,tem_low,color='blue',label='低溫')    # 畫出低溫度曲線
  plt.scatter(x,tem_low,color='blue')     # 點出每個時刻的溫度點
  
  plt.plot([1, 15], [tem_high_ave, tem_high_ave], c='black', linestyle='--')  # 畫出平均溫度虛線
  plt.plot([1, 15], [tem_low_ave, tem_low_ave], c='black', linestyle='--')  # 畫出平均溫度虛線
  plt.legend()
  plt.text(tem_max_date+0.15, tem_max+0.15, str(tem_max), ha='center', va='bottom', fontsize=10.5)  # 標出最高溫度
  plt.text(tem_min_date+0.15, tem_min+0.15, str(tem_min), ha='center', va='bottom', fontsize=10.5)  # 標出最低溫度
  plt.xticks(x)
  plt.title('未來14天高溫低溫變化曲線圖')
  plt.xlabel('未來天數/天')
  plt.ylabel('攝氏度/°C')
  plt.show()
def change_wind(wind):
  """改變風向"""
  for i in range(0,14):
    if wind[i] == "北風":
      wind[i] = 90
    elif wind[i] == "南風":
      wind[i] = 270
    elif wind[i] == "西風":
      wind[i] = 180
    elif wind[i] == "東風":
      wind[i] = 360
    elif wind[i] == "東北風":
      wind[i] = 45
    elif wind[i] == "西北風":
      wind[i] = 135
    elif wind[i] == "西南風":
      wind[i] = 225
    elif wind[i] == "東南風":
      wind[i] = 315
  return wind

def wind_radar(data):
  """風向雷達圖"""
  wind1 = list(data['風向1'])
  wind2 = list(data['風向2'])
  wind_speed = list(data['風級'])
  wind1 = change_wind(wind1)
  wind2 = change_wind(wind2)
  
  degs = np.arange(45,361,45)
  temp = []
  for deg in degs:
    speed = []
    # 獲取 wind_deg 在指定範圍的風速平均值資料
    for i in range(0,14):
      if wind1[i] == deg:
        speed.append(wind_speed[i])
      if wind2[i] == deg:
        speed.append(wind_speed[i])
      if len(speed) == 0:
        temp.append(0)
      else:
        temp.append(sum(speed)/len(speed))
  print(temp)
  N = 8
  theta = np.arange(0.+np.pi/8,2*np.pi+np.pi/8,2*np.pi/8)
  # 數據極徑
  radii = np.array(temp)
  # 繪製極區圖坐標系
  plt.axes(polar=True)
  # 定義每個磁區的RGB值（R,G,B），x越大，對應的顏色越接近藍色
  colors = [(1-x/max(temp), 1-x/max(temp),0.6) for x in radii]
  plt.bar(theta,radii,width=(2*np.pi/N),bottom=0.0,color=colors)
  plt.title('未來14天風級圖',x=0.2,fontsize=20)
  plt.show()

def weather_pie(data):
  """繪製天氣圓形圖"""
  weather = list(data['天氣'])
  dic_wea = {'<!--' and '-->' }
  for i in range(0,14):
    if weather[i] in dic_wea.keys():
      dic_wea[weather[i]] += 1
    else:
      dic_wea[weather[i]] = 1
  print(dic_wea)
  explode=[0.01]*len(dic_wea.keys())
  color = ['lightskyblue','silver','yellow','salmon','grey','lime','gold','red','green','pink']
  plt.pie(dic_wea.values(),explode=explode,labels=dic_wea.keys(),autopct='%1.1f%%',colors=color)
  plt.title('未來14天氣候分佈圓形圖')
  plt.show()

def main():
  plt.rcParams['font.sans-serif']=['Noto Sans TC'] # 解決中文顯示問題
  plt.rcParams['axes.unicode_minus'] = False  # 解決負號顯示問題
  data14 = pd.read_csv('weather14.csv',encoding='UTF-8')
  print(data14)
  '''tem_curve(data14)'''
  wind_radar(data14)
  weather_pie(data14)

if __name__ == '__main__':
  main()

