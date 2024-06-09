# test_parse.py

import pytest
from json_parser import parse_value

def test_parse_value_string():
    tokens = ['"hello"']
    result = parse_value(tokens)
    assert result == "hello"

def test_parse_value_number():
    tokens = ['123']
    result = parse_value(tokens)
    assert result == 123

def test_parse_value_boolean_true():
    tokens = ['true']
    result = parse_value(tokens)
    assert result == True

def test_parse_value_boolean_false():
    tokens = ['false']
    result = parse_value(tokens)
    assert result == False

def test_parse_value_null():
    tokens = ['null']
    result = parse_value(tokens)
    assert result == None

def test_parse_value_object():
    tokens = ['{', '"key"', ':', '"value"', '}']
    result = parse_value(tokens)
    assert result == {"key": "value"}

def test_parse_value_array():
    tokens = ['[', '"item1"', ',', '"item2"', ']']
    result = parse_value(tokens)
    assert result == ["item1", "item2"]

def test_parse_value_invalid():
    tokens = ['invalid']
    with pytest.raises(ValueError) as e:
        parse_value(tokens)
    assert str(e.value) == "Invalid value: invalid"