#0c45f909abe580009e821ecdb47cfa43
import requests
import csv
from pprint import pprint

airport_name = input('enter the airport name: ')

city = ''

with open('airports.csv', 'r') as airportsfile:

	airportsreader = csv.reader(airportsfile, delimiter = ',')

	for row in airportsreader:

		if (row[3] == airport_name and row[10] != ''):

			city = row[10]

			break

#print(city)

url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=0c45f909abe580009e821ecdb47cfa43&units=metric'.format(city)

res = requests.get(url)

data = res.json()

temp = data['main']['temp']

print(airport_name + ' current temperature: ' + str(temp))