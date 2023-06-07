# data1_analysis.py
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
np.seterr(divide='ignore',invalid='ignore') #https://zhuanlan.zhihu.com/p/164619774避免error
def tem_curve(data):
  """溫度曲線繪製"""
  hour = list(data['小時'])
  tem = list(data['溫度'])
  for i in range(0,24):
    if math.isnan(tem[i]) == True:
      tem[i] = tem[i-1]
  tem_ave = sum(tem)/24     # 求平均溫度  
  tem_max = max(tem)    
  tem_max_hour = hour[tem.index(tem_max)] # 求最高溫度
  tem_min = min(tem)
  tem_min_hour = hour[tem.index(tem_min)] # 求最低溫度
  x = []
  y = []
  for i in range(0, 24):
    x.append(i)
    y.append(tem[hour.index(i)])
  plt.figure(1)
  plt.plot(x,y,color='red',label='溫度')       # 畫出溫度曲線
  plt.scatter(x,y,color='red')   # 點出每個時刻的溫度點
  plt.plot([0, 24], [tem_ave, tem_ave], c='blue', linestyle='--',label='平均溫度')  # 畫出平均溫度虛線
  plt.text(tem_max_hour+0.15, tem_max+0.15, str(tem_max), ha='center', va='bottom', fontsize=10.5)  # 標出最高溫度
  plt.text(tem_min_hour+0.15, tem_min+0.15, str(tem_min), ha='center', va='bottom', fontsize=10.5)  # 標出最低溫度
  plt.xticks(x)
  plt.legend()
  plt.title('一天溫度變化曲線圖')
  plt.xlabel('時間/h')
  plt.ylabel('攝氏度/°C')
  plt.show()
def hum_curve(data):
  """相對濕度曲線繪製"""
  hour = list(data['小時'])
  hum = list(data['相對濕度'])
  for i in range(0,24):
    if math.isnan(hum[i]) == True:
      hum[i] = hum[i-1]
  hum_ave = sum(hum)/24     # 求平均相對濕度  
  hum_max = max(hum)    
  hum_max_hour = hour[hum.index(hum_max)] # 求最高相對濕度
  hum_min = min(hum)
  hum_min_hour = hour[hum.index(hum_min)] # 求最低相對濕度
  x = []
  y = []
  for i in range(0, 24):
    x.append(i)
    y.append(hum[hour.index(i)])
  plt.figure(2)
  plt.plot(x,y,color='blue',label='相對濕度')       # 畫出相對濕度曲線
  plt.scatter(x,y,color='blue')   # 點出每個時刻的相對濕度
  plt.plot([0, 24], [hum_ave, hum_ave], c='red', linestyle='--',label='平均相對濕度')  # 畫出平均相對濕度虛線
  plt.text(hum_max_hour+0.15, hum_max+0.15, str(hum_max), ha='center', va='bottom', fontsize=10.5)  # 標出最高相對濕度
  plt.text(hum_min_hour+0.15, hum_min+0.15, str(hum_min), ha='center', va='bottom', fontsize=10.5)  # 標出最低相對濕度
  plt.xticks(x)
  plt.legend()
  plt.title('一天相對濕度變化曲線圖')
  plt.xlabel('時間/h')
  plt.ylabel('百分比/%')
  plt.show()
def air_curve(data):
  """空氣品質曲線繪製"""
  hour = list(data['小時'])
  air = list(data['空氣品質']) #空气质量 #空氣品質
  print(type(air[0]))
  for i in range(0,24):
    if math.isnan(air[i]) == True:
      air[i] = air[i-1]
  air_ave = sum(air)/24     # 求平均空氣品質  
  air_max = max(air)    
  air_max_hour = hour[air.index(air_max)] # 求最高空氣品質
  air_min = min(air)
  air_min_hour = hour[air.index(air_min)] # 求最低空氣品質
  x = []
  y = []
  for i in range(0, 24):
    x.append(i)
    y.append(air[hour.index(i)])
  plt.figure(3)

  for i in range(0,24):
    if y[i] <= 50:
      plt.bar(x[i],y[i],color='lightgreen',width=0.7)  # 1等級
    elif y[i] <= 100:
      plt.bar(x[i],y[i],color='wheat',width=0.7)   # 2等級
    elif y[i] <= 150:
      plt.bar(x[i],y[i],color='orange',width=0.7)   # 3等級
    elif y[i] <= 200:
      plt.bar(x[i],y[i],color='orangered',width=0.7)  # 4等級
    elif y[i] <= 300:
      plt.bar(x[i],y[i],color='darkviolet',width=0.7)  # 5等級
    elif y[i] > 300:
      plt.bar(x[i],y[i],color='maroon',width=0.7)   # 6等級
  plt.plot([0, 24], [air_ave, air_ave], c='black', linestyle='--')  # 畫出平均空氣品質虛線
  plt.text(air_max_hour+0.15, air_max+0.15, str(air_max), ha='center', va='bottom', fontsize=10.5)  # 標出最高空氣品質
  plt.text(air_min_hour+0.15, air_min+0.15, str(air_min), ha='center', va='bottom', fontsize=10.5)  # 標出最低空氣品質
  plt.xticks(x)
  plt.title('一天空氣品質變化曲線圖')
  plt.xlabel('時間/h')
  plt.ylabel('空氣品質指數AQI')
  plt.show()
def wind_radar(data):
  """風向雷達圖"""
  wind = list(data['風力方向'])
  wind_speed = list(data['風級'])
  for i in range(0,24):
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
    degs = np.arange(45,361,45)
    temp = []
  for deg in degs:
    speed = []
    # 獲取 wind_deg 在指定範圍的風速平均值資料
    for i in range(0,24):
      if wind[i] == deg:
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
  # 繪製極區圖座標系
  plt.axes(polar=True)
  # 定義每個磁區的RGB值（R,G,B），x越大，對應的顏色越接近藍色
  colors = [(1-x/max(temp), 1-x/max(temp),0.6) for x in radii]
  plt.bar(theta, radii, width=(2*np.pi/N), bottom=0.0,color='lightblue')
  plt.title('一天風級圖',x=0.2,fontsize=20)
  plt.show()
def calc_corr(a, b):
  """計算相關係數"""
  a_avg = sum(a)/len(a)
  b_avg = sum(b)/len(b)
  cov_ab = sum([(x - a_avg)*(y - b_avg) for x,y in zip(a, b)])
  sq = math.sqrt(sum([(x - a_avg)**2 for x in a])*sum([(x - b_avg)**2 for x in b]))  
  corr_factor = cov_ab/sq
  return corr_factor
def corr_tem_hum(data):
  """溫濕度相關性分析"""
  tem = data['溫度']
  hum = data['相對濕度']
  plt.scatter(tem,hum,color='blue')
  plt.title("溫濕度相關性分析圖")
  plt.xlabel("溫度/°C")
  plt.ylabel("相對濕度/%")
  plt.text(20,40,"相關係數為："+str(calc_corr(tem,hum)),fontdict={'size':'10','color':'red'})
  plt.show()
  print(f"相關係數為："+str(calc_corr(tem,hum)))
def main():
  plt.rcParams['font.sans-serif']=['Noto Sans TC'] # 解決中文顯示問題
  data1 = pd.read_csv('weather1.csv', encoding='UTF-8')
  print(data1)
  tem_curve(data1)
  hum_curve(data1)
  air_curve(data1)
  wind_radar(data1)
  corr_tem_hum(data1)
if __name__ == '__main__':
  main()

