# test_json_parser.py

import pytest
from json_parser import parser, lexer

# Define the paths to the valid and invalid JSON files
valid_json_files = [
    'tests/step1/valid.json',
    'tests/step2/valid.json',
    'tests/step2/valid2.json',
    'tests/step3/valid.json',
    'tests/step4/valid.json',
    'tests/step4/valid2.json',
    'tests/final_test/test/pass1.json',
    'tests/final_test/test/pass2.json',
    'tests/final_test/test/pass3.json',
    ]
invalid_json_files = [
    'tests/step1/invalid.json',
    'tests/step2/invalid.json',
    'tests/step2/invalid2.json',
    'tests/step3/invalid.json',
    'tests/step4/invalid.json',
    'tests/final_test/test/fail1.json',
    'tests/final_test/test/fail2.json',
    'tests/final_test/test/fail3.json',
    'tests/final_test/test/fail4.json',
    'tests/final_test/test/fail5.json',
    'tests/final_test/test/fail6.json',
    'tests/final_test/test/fail7.json',
    'tests/final_test/test/fail8.json',
    'tests/final_test/test/fail9.json',
    'tests/final_test/test/fail10.json',
    'tests/final_test/test/fail11.json',
    'tests/final_test/test/fail12.json',
    'tests/final_test/test/fail13.json',
    'tests/final_test/test/fail14.json',
    'tests/final_test/test/fail15.json',
    'tests/final_test/test/fail16.json',
    'tests/final_test/test/fail17.json',
    'tests/final_test/test/fail18.json',
    'tests/final_test/test/fail19.json',
    'tests/final_test/test/fail20.json',
    'tests/final_test/test/fail21.json',
    'tests/final_test/test/fail22.json',
    'tests/final_test/test/fail23.json',
    'tests/final_test/test/fail24.json',
    'tests/final_test/test/fail25.json',
    'tests/final_test/test/fail26.json',
    'tests/final_test/test/fail27.json',
    'tests/final_test/test/fail28.json',
    'tests/final_test/test/fail29.json',
    'tests/final_test/test/fail30.json',
    'tests/final_test/test/fail31.json',
    'tests/final_test/test/fail32.json',
    'tests/final_test/test/fail33.json'
    ]

@pytest.mark.parametrize('file_path', valid_json_files)
def test_valid_json(file_path):
    with open(file_path, 'r') as f:
        json_string = f.read()
        # Tokenize the JSON string
        tokens = lexer(json_string)
        # Parse the tokens into a Python dictionary
        try:
            json_object = parser(tokens)
            # The result should be a dictionary
            assert isinstance(json_object, dict)
        except ValueError as e:
            pytest.fail(str(e))
            
@pytest.mark.parametrize('file_path', invalid_json_files)
def test_invalid_json(file_path):
    with open(file_path, 'r') as f:
        json_string = f.read()
        try:
            # Tokenize the JSON string
            tokens = lexer(json_string)
        except ValueError as e:
            assert str(e) == "Lexer - Empty JSON string."