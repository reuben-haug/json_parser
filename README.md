# JSON Parser
![Build Status](https://img.shields.io/travis/reuben-haug/json_parser/main)
![Coverage](https://img.shields.io/codecov/c/github/reuben-haug/json_parser)
![License](https://img.shields.io/github/license/reuben-haug/json_parser)
![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)
![Last Commit](https://img.shields.io/github/last-commit/reuben-haug/json_parser)

Provides a simple JSON parser that can parse JSON strings into Python dictionaries. It also includes utility functions for cleaning and validating JSON strings.

## Functions

Here are the main functions provided by this module:

- `lexer(json_string)`: Tokenizes the input JSON string into a list of tokens.
- `parser(tokens)`: Parses a list of tokens into a Python dictionary.
- `clean_tokens(tokens)`: Cleans the tokens by removing leading and trailing whitespace.
- `parse_key(token)`: Parses a key from a token.
- `parse_value(tokens)`: Parses a value from a list of tokens.
- `parse_object(tokens)`: Parses an object from a list of tokens.
- `parse_array(tokens)`: Parses an array from a list of tokens.
- `remove_quotes(token)`: Removes the leading and trailing double quotes from a token.
- `clean_key(token)`: Cleans a key token by removing leading and trailing whitespaces.
- `clean_value(token)`: Cleans a value based on its type.
- `is_valid_json_object(string)`: Checks if a string is a valid JSON object.
- `has_key_value_pairs(json_object)`: Identifies if there are key-value pairs in a JSON string.

## Usage

To use this module, import it into your Python script and call the `lexer` and `parser` functions to parse a JSON string into a Python dictionary.

## Testing

Tests for this module are located in the `tests` folder. Use `test_json_parser.py` to test valid and invalid JSON strings.  Use `test_parse.py` to test the `parse_value` function.

## Contributing

Contributions are welcome. Please submit a pull request with any enhancements or bug fixes.

## License

This project is licensed under the MIT License.