#0c45f909abe580009e821ecdb47cfa43
import requests
import csv
from pprint import pprint

city = input('enter the city name: ')

url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=0c45f909abe580009e821ecdb47cfa43&units=metric'.format(city)

with open('airports.csv', 'r') as airportsfile:
	airportsreader = csv.reader()
res = requests.get(url)

data = res.json()

pprint(data)