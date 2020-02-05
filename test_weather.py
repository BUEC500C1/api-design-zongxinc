from weather import weather

def test():
	assert weather('York Airport') != 'no airport found'
	assert weather('jkhkzdhkfhds') == 'no airport found'
	assert weather('Hammer Airport') != 'no airport found'
	