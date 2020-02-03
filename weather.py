#0c45f909abe580009e821ecdb47cfa43
import requests
import csv
import math
from pprint import pprint

airport_name = input('enter the airport name: ')


with open('airports.csv', 'r') as airportsfile:

	airportsreader = csv.reader(airportsfile, delimiter = ',')

	for row in airportsreader:

		if row[3] == airport_name:

			latitude = row[4]

			longtitude = row[5]

			break

#print(city)

#url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=0c45f909abe580009e821ecdb47cfa43&units=metric'.format(city)

url = 'https://api.weather.gov/points/' + str(latitude) + ',' + str(longtitude)

res = requests.get(url)

data = res.json()

myurl = data['properties']['observationStations']

res = requests.get(myurl)

data = res.json()

observationurl = data['features'][0]['id'] + '/observations'

res = requests.get(observationurl)

data = res.json()

#print(data['features'])
count = 1

for elements in data['features']:

	print('date: ' + elements['properties']['timestamp'][0:10] + '  ' + 'time: '+ elements['properties']['timestamp'][11:16] + '  ' + 'temperature: ' + str(math.trunc(elements['properties']['temperature']['value'])) + ' Celsius')

	count = count + 1

	if count > 24:

		break

#pprint(data)

#temp = data['main']['temp']

#print(airport_name + ' current temperature: ' + str(temp))