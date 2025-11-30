import pytest
from src.lexer import Lexer

def test_number_token():
    lexer = Lexer("123 456")
    tokens = lexer.generate_tokens()
    assert tokens == [('NUMBER', '123'), ('NUMBER', '456')]

def test_array_tokens():
    lexer = Lexer("#(1,2,3)")
    tokens = lexer.generate_tokens()
    assert tokens[0] == ('ARRAY_START', '#')
    assert tokens[1] == ('LPAREN', '(')
    assert tokens[-1] == ('RPAREN', ')')
