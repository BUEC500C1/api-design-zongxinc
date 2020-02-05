from io import StringIO
from weather import main

airport_name = StringIO('York Airport\n')

def test_1(monkeypatch):

	#input_values = 'York Airport\n'
 
	#weather.input = input_values
	monkeypatch.setattr('sys.stdin', airport_name)

	assert main() != 'no airport found'

airport_name1 = StringIO('jkhkzdhkfhds\n')

def test_2(monkeypatch):
	
	monkeypatch.setattr('sys.stdin', airport_name1)

	assert main() == 'no airport found'

airport_name2 = StringIO('Hammer Airport\n')

def test_3(monkeypatch):

	monkeypatch.setattr('sys.stdin', airport_name2)

	assert main() != 'no airport found'
	