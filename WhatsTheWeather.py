import requests
from pprint import pprint

API_Key = '8dc485de28844db57de5bc9ddbccf9d2'

city = input("Enter a city: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city

weather_data = requests.get(base_url).json()

pprint(weather_data)
