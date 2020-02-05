from io import StringIO
from weather import weather

airport_name = StringIO('York Airport\n')

def test_1(monkeypatch):

	monkeypatch.setattr('sys.stdin', airport_name)

	assert weather('York Airport') != 'no airport found'

airport_name = StringIO('jkhkzdhkfhds')

def test_2(monkeypatch):
	
	monkeypatch.setattr('sys.stdin', airport_name)

	assert weather('jkhkzdhkfhds') == 'no airport found'

airport_name = StringIO('Hammer Airport')

def test_3(monkeypatch):
	
	monkeypatch.setattr('sys.stdin', airport_name)

	assert weather('Hammer Airport') != 'no airport found'
	