from src.parser import Parser

def test_parse_number():
    assert Parser("123").parse() == 123

def test_parse_array():
    assert Parser("#(1,2,3)").parse() == [1, 2, 3]

def test_parse_dict():
    assert Parser("{x=>1,y=>2}").parse() == {'x': 1, 'y': 2}
