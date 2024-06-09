'''
Coding challenge JSON parser from https://codingchallenges.fyi/challenges/challenge-json-parser.
'''
import re


def lexer(json_string):
    """
    Tokenizes the input JSON string.
    
    Args: json_string (str): The input JSON string.
    
    Returns: tokens (list): A list of tokens extracted from the JSON string.
    """
    if not json_string:
        raise ValueError("Lexer - Empty JSON string.")
    pattern = r'\".*?\"|\d+|true|false|null|[\{\}\:\,]'
    tokens = re.findall(pattern, json_string)
    return tokens


def parser(tokens):
    '''Parse a list of tokens into a Python dictionary.'''
    json_object = {}
    while tokens:
        token = tokens.pop(0)
        if token == '{':
            # If the next token is '}', it's an empty JSON object
            if tokens and tokens[0] == '}':
                tokens.pop(0) # Remove the '}' token
                return json_object
            key_token = tokens.pop(0)
            key = parse_key(key_token)
            if key is None:
                raise ValueError(f"Error parsing key: {key_token}")
            if not tokens:
                raise ValueError(f"Error: Expected a value after key, got None.")
            if tokens.pop(0) != ':':
                tokens.pop(0)
            value_token = tokens.pop(0)
            try:
                if isinstance(value_token, str):
                    value_token = [value_token]
                value = parse_value(value_token)
            except ValueError:
                raise ValueError(f"Error parsing value: {value_token}")
            json_object[key] = value
            # Check for trailing comma
            if tokens and tokens[0] == ',':
                tokens.pop(0)
                if not tokens or tokens[0] == '}':
                    raise ValueError(f"Error: Trailing comma after key-value pair.")
    return json_object


def clean_tokens(tokens):
    '''Clean the tokens by removing leading and trailing whitespace.'''
    return [token.strip() for token in tokens]


def parse_key(token):
    '''Parse a key from a token.'''
    return clean_key(token)


def parse_value(tokens):
    '''Parse a value from a list of tokens.'''
    if not tokens:
        raise ValueError("Unexpected end of tokens while parsing value.")
    token = tokens.pop(0)
    if token == '{':
        return parse_object(tokens)
    elif token == '[':
        return parse_array(tokens)
    else:
        return clean_value(token)
    

def parse_object(tokens):
    '''Parse an object from a list of tokens.'''
    obj = {}
    if not tokens: # Check if the tokens list is empty
        return obj
    token = tokens.pop(0)
    while token != '}':
        key = clean_value(token)
        tokens.pop(0) # Remove the ':' token
        value = parse_value(tokens)
        obj[key] = value
        if not tokens: 
            break
        token = tokens.pop(0)
        if token == ',':
            token = tokens.pop(0)
    return obj


def parse_array(tokens):
    '''Parse an array from a list of tokens.'''
    arr = []
    token = tokens.pop(0)
    while token != ']':
        value = parse_value([token])
        arr.append(value)
        token = tokens.pop(0)
        if token == ',':
            token = tokens.pop(0)
    return arr


def remove_quotes(token):
    '''Remove the leading and trailing double quotes from a token.'''
    if token[0] == '"' and token[-1] == '"':
        return token[1:-1]
    return token


def clean_key(token):
    '''Clean a key token by removing leading and trailing whitespaces.'''
    cleaned_token = token.strip()
    if cleaned_token[0] != '"' or cleaned_token[-1] != '"':
        raise ValueError(f"Invalid key: {token}")
    return remove_quotes(cleaned_token)


def clean_value(token):
    '''Clean a value based on it's type.'''
    if token[0] == '"' and token[-1] == '"':
        return remove_quotes(token)
    elif token == 'null':
        return None
    elif token == 'true':
        return True
    elif token == 'false':
        return False
    else:
        try:
            return int(token)
        except ValueError:
            try:
                return float(token)
            except ValueError:
                raise ValueError(f"Invalid value: {token}")


def is_valid_json_object(string):
    '''
    Check if a string is a valid JSON object.
    
    Args: string (str): The input string.
    
    Returns: bool: True if the string is a valid JSON object, False otherwise.
    '''
    tokens = lexer(string)
    if not tokens:
        return False
    if not (tokens[0] == '{' and tokens[-1] == '}'):
        return False
    for i in range(1, len(tokens) - 1):
        if tokens[i] == ':':
            try:
                parse_key(tokens[i - 1])
                parse_value(tokens[i + 1])
            except ValueError as e:
                print(f"Error parsing key or value: {e}")
                return False
    return True


def has_key_value_pairs(json_object):
    '''
    Identify if there are key-value pairs in a JSON string.
    
    Args: json_string (dict): The input JSON object.
    
    Returns: bool: True if the JSON object contains key-value pairs, False otherwise.
    '''
    return bool(json_object)