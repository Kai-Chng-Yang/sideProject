import requests

county_list = None

def getInfo():
    global county_list
    url = "https://data.epa.gov.tw/api/v2/aqx_p_432?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=ImportDate desc&format=JSON"
    response = requests.get(url)
    data_list = response.json()
    county_temp = set()
    for item in data_list:
        county_temp.add(item["county"])
    county_list = list(county_temp)


getInfo()
