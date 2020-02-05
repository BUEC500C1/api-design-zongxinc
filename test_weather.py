from weather import weather

def test():
	weather.input() = lambda: 'York Airport'
	assert weather('York Airport') != 'no airport found'
	weather.input() = lambda: 'jkhkzdhkfhds'
	assert weather('jkhkzdhkfhds') == 'no airport found'
	weather.input() = lambda: 'Hammer Airport'
	assert weather('Hammer Airport') != 'no airport found'
	