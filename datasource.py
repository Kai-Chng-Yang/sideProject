import requests

sarea_list = None
data_list = None

def getInfo():
    global sarea_list, data_list
    url = 'https://data.epa.gov.tw/api/v2/aqx_p_432?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=ImportDate desc&format=JSON'
    response = requests.get(url)
    data_list = response.json()
    sarea_temp = set()
    for item in data_list:
        sarea_temp.add(item["sarea"])
    sarea_list = sorted(list(sarea_temp))

def getInfoFromArea(areaName) -> list:
    filter_data = filter(lambda n:n["sarea"]==areaName,data_list)
    return list(filter_data)
    
def filter_sbi_warning_data(area_data,numbers) -> list:
    filter_data = filter(lambda n:n['sbi']<=numbers,area_data)
    return list(filter_data)

def filter_bemp_warning_data(area_data, numbers) -> list:
    filter_data = filter(lambda n: n['bemp'] <=numbers, area_data)
    return list(filter_data)

getInfo()