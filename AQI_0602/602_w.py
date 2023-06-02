# weather.py
import requests
from bs4 import BeautifulSoup
import csv
import json
#from html.parser import HTMLParser

def getHTMLtext(url):     
 """請求獲得網頁內容"""
 try:         
  r = requests.get(url, timeout = 30)         
  r.raise_for_status()         
  r.encoding = r.apparent_encoding         
  print("成功訪問")         
  return r.text     
 except:         
  print("訪問錯誤")         
  return" " 

def get_content(html):
 """處理得到有用信息保存數據文件"""
 final = []          # 初始化一個列表保存數據
 bs = BeautifulSoup(html, "html.parser")  # 創建BeautifulSoup對象
 body = bs.body
 #data = body.find('div', {<!-- -->'id':'7d'})    # 找到div標簽且id = 7d
 data = body.find("div", {"id":"7d"})    # 找到div標簽且id = 7d OKOK
 # 下面爬取當天的數據
 data2 = body.find_all('div',{'class':'left-div'})
 text = data2[2].find('script').string  
 text = text[text.index('=')+1 :-2]   # 移除改var data=將其變為json數據
 jd = json.loads(text)
 dayone = jd['od']['od2']     # 找到當天的數據
 final_day = []           # 存放當天的數據
 count = 0
 for i in dayone:
  temp = []
  if count <=23:
   temp.append(i['od21'])     # 添加時間
   temp.append(i['od22'])     # 添加當前時刻溫度
   temp.append(i['od24'])     # 添加當前時刻風力方向
   temp.append(i['od25'])     # 添加當前時刻風級
   temp.append(i['od26'])     # 添加當前時刻降水量
   temp.append(i['od27'])     # 添加當前時刻相對濕度
   temp.append(i['od28'])     # 添加當前時刻控制質量
   #print(temp)
   final_day.append(temp)
  count = count +1
 # 下麵爬取7天的數據 
 ul = data.find('ul')      # 找到所有的ul標簽
 li = ul.find_all('li')      # 找到左右的li標簽
 i = 0     # 控制爬取的天數
 for day in li:          # 遍歷找到的每一個li
     if i < 7 and i > 0:
         temp = []          # 臨時存放每天的數據
         date = day.find('h1').string     # 得到日期
         date = date[0:date.index('日')]   # 取出日期號
         temp.append(date)            
         inf = day.find_all('p')      # 找出li下面的p標簽,提取第一個p標簽的值，即天氣
         temp.append(inf[0].string)

         tem_low = inf[1].find('i').string   # 找到最低氣溫

         if inf[1].find('span') is None:   # 天氣預報可能沒有最高氣溫
             tem_high = None
         else:
             tem_high = inf[1].find('span').string  # 找到最高氣溫
         temp.append(tem_low[:-1])
         if tem_high[-1] == '℃':
          temp.append(tem_high[:-1])
         else:
          temp.append(tem_high)

         wind = inf[2].find_all('span')  # 找到風向
         for j in wind:
          temp.append(j['title'])

         wind_scale = inf[2].find('i').string # 找到風級
         index1 = wind_scale.index('级')
         temp.append(int(wind_scale[index1-1:index1]))
         final.append(temp)
     i = i + 1
 return final_day,final
 #print(final)    
def get_content2(html):
 """處理得到有用信息保存數據文件"""
 final = []                # 初始化一個列表保存數據
 bs = BeautifulSoup(html, "html.parser")        # 創建BeautifulSoup對象
 body = bs.body
 data = body.find('div', {'id': '15d'})          # 找到div標簽且id = 15d OKOK
 #data = body.find('div', {<!-- -->'id': '15d'})          # 找到div標簽且id = 15d
 ul = data.find('ul')            # 找到所有的ul標簽
 li = ul.find_all('li')            # 找到左右的li標簽
 final = []
 i = 0                 # 控制爬取的天數
 for day in li:               # 遍歷找到的每一個li
     if i < 8:
         temp = []               # 臨時存放每天的數據
         date = day.find('span',{'class':'time'}).string    # 得到日期 OKOK
#         date = day.find('span',{<!-- -->'class':'time'}).string    # 得到日期         
         date = date[date.index('（')+1:-2]        # 取出日期號
         temp.append(date)  
         weather = day.find('span',{'class':'wea'}).string    # 找到天氣OK
#         weather = day.find('span',{<!-- -->'class':'wea'}).string    # 找到天氣
         temp.append(weather)
         tem = day.find('span',{'class':'tem'}).text      # 找到溫度OK
#         tem = day.find('span',{<!-- -->'class':'tem'}).text      # 找到溫度
         temp.append(tem[tem.index('/')+1:-1])     # 找到最低氣溫
         temp.append(tem[:tem.index('/')-1])      # 找到最高氣溫
         wind = day.find('span',{'class':'wind'}).string    # 找到風向OK
#         wind = day.find('span',{<!-- -->'class':'wind'}).string    # 找到風向
         if '轉' in wind:           # 如果有風向變化
          temp.append(wind[:wind.index('轉')])
          temp.append(wind[wind.index('轉')+1:])
         else:             # 如果沒有風向變化，前後風向一致
          temp.append(wind)
          temp.append(wind)
         wind_scale = day.find('span',{'class':'wind1'}).string    # 找到風級OK
#         wind_scale = day.find('span',{<!-- -->'class':'wind1'}).string    # 找到風級
         index1 = wind_scale.index('级')
         temp.append(int(wind_scale[index1-1:index1]))
          
         final.append(temp)
 return final

def write_to_csv(file_name, data, day=14):
 """保存為csv文件"""
 with open(file_name, 'a', errors='ignore', newline='') as f:
  if day == 14:
   header = ['日期','天氣','最低氣溫','最高氣溫','風向1','風向2','風級']
  else:
   header = ['小時','溫度','風力方向','風級','降水量','相對濕度','空氣質量']
  f_csv = csv.writer(f)
  f_csv.writerow(header)
  f_csv.writerows(data)

def main():
 """主函數"""
 print("Weather test")
 # 台北
 url1 = 'http://www.weather.com.cn/weather/101340101.shtml'    # 7天天氣中國天氣網
 url2 = 'http://www.weather.com.cn/weather15d/101340101.shtml' # 8-15天天氣中國天氣網
 
 html1 = getHTMLtext(url1)
 data1, data1_7 = get_content(html1)  # 獲得1-7天和當天的數據

 html2 = getHTMLtext(url2)
 data8_14 = get_content2(html2)   # 獲得8-14天數據
 data14 = data1_7 + data8_14
 #print(data)
 write_to_csv('weather14.csv',data14,14) # 保存為csv文件
 write_to_csv('weather1.csv',data1,1)

if __name__ == '__main__':
 main()