import pytest
from src.lexer import Lexer

def test_number_token():
    lexer = Lexer("123 456")
    tokens = lexer.generate_tokens()
    assert tokens == [('NUMBER', '123'), ('NUMBER', '456')]
