import requests
import json


def weather_data():
    url = "https://api.openweathermap.org/data/2.5/weather?lat=23.68&lon=90.35&appid=f4fd58272f8be928ccb68c851b616187&units=metric"

    res = requests.get(url)
    string_res = res.content.decode('UTF-8')
    dic_res = json.loads(string_res)
    
    print(f"Location: {dic_res['name']}")
    print(f'Current Temperature: {dic_res["main"]["temp"]}')
    print(f'Feels like: {dic_res["main"]["feels_like"]}')
    print(f'Minimum temperature: {dic_res["main"]["temp_min"]}')
    print(f'Maximum temperature: {dic_res["main"]["temp_max"]}')
    print(f'Humidity: {dic_res["main"]["humidity"]}')
    

weather_data()
