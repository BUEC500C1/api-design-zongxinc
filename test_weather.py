from io import StringIO
from weather import main

airport_name = StringIO('York Airport\n')

def test_1(monkeypatch):

	#input_values = 'York Airport\n'
 
	#weather.input = input_values
	monkeypatch.setattr('sys.stdin', airport_name)

	assert main() != 'no airport found'

airport_name = StringIO('jkhkzdhkfhds\n')

def test_2(monkeypatch):
	
	monkeypatch.setattr('sys.stdin', airport_name)

	assert main() == 'no airport found'

#airport_name = StringIO('Hammer Airport')

#def test_3(monkeypatch):

	#monkeypatch.setattr('sys.stdin', airport_name)

	#assert weather('Hammer Airport') != 'no airport found'
	