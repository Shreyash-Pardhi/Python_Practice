import datetime
import requests

city = input("Enter city name: ")

try:
    res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=999c7d88f8d5f08484a690a919d4c9c9")
    print(f"Tempreture: {res.json()['main']['temp']}")
    print(f"Date & Time: {datetime.datetime.fromtimestamp(res.json()['dt']).strftime('%Y-%m-%d %H:%M:%S')}")
    
except Exception as _:
    print("City not Found!!!")
