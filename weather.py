#0c45f909abe580009e821ecdb47cfa43
import requests
import csv
import math
from pprint import pprint



def weather():

	airport_name = input('enter the airport name: ')

	latitude = 0

	longtitude = 0

	with open('airports.csv', 'r') as airportsfile:

		airportsreader = csv.reader(airportsfile, delimiter = ',')

		for row in airportsreader:

			if row[3] == airport_name:

				latitude = row[4]

				longtitude = row[5]

				break

		if (longtitude == 0 and latitude == 0):

			return 'no airport found'

	url = 'https://api.weather.gov/points/' + str(latitude) + ',' + str(longtitude)

	res = requests.get(url)

	data = res.json()

	myurl = data['properties']['observationStations']

	res = requests.get(myurl)

	data = res.json()

	observationurl = data['features'][0]['id'] + '/observations'

	res = requests.get(observationurl)

	data = res.json()

	return data['features']

count = 1

if weather(airport_name) == 'no airport found':
	
	print('no airport found')

else:

	for elements in weather(airport_name):

		print('date: ' + elements['properties']['timestamp'][0:10] + '  ' + 'time: '+ elements['properties']['timestamp'][11:16] + '  ' + 'temperature: ' + str(math.trunc(elements['properties']['temperature']['value'])) + ' Celsius')

		count = count + 1

		if count > 24:

			break

#return 1
