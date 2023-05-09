import requests

def getInfo() -> None:
    
    # Get data from TCGB website
    htmldata = getdata("https://weather.com/zh-TW/forecast/air-quality/l/6b221b26e046a442e03dc46fbe91d5874c6461afde61187dd4126bddeea1e2aa")
    response = requests.get(htmldata)
    print(response.text)