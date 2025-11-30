from typing import List, Union, Tuple
from src.lexer import Lexer, Token

Value = Union[int, list, dict]

class Parser:
    def __init__(self, text: str):
        self.tokens = Lexer(text).generate_tokens()
        self.pos = 0
        self.current_token = self.tokens[self.pos] if self.tokens else None

    def advance(self):
        self.pos += 1
        self.current_token = self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def parse(self) -> Value:
        if not self.current_token:
            return None
        if self.current_token[0] == 'NUMBER':
            val = int(self.current_token[1])
            self.advance()
            return val
        elif self.current_token[0] == 'ARRAY_START':
            return self.parse_array()
        elif self.current_token[0] == 'LBRACE':
            return self.parse_dict()
        # Для простоты — поддержка констант может быть добавлена позже
        return None

    def parse_array(self) -> list:
        arr = []
        self.advance()  # пропускаем '#'
        if self.current_token[0] != 'LPAREN':
            raise SyntaxError("Ожидается '(' после '#'")
        self.advance()
        while self.current_token and self.current_token[0] != 'RPAREN':
            if self.current_token[0] == 'NUMBER':
                arr.append(int(self.current_token[1]))
                self.advance()
            elif self.current_token[0] == 'CHAR' and self.current_token[1] == ',':
                self.advance()
            else:
                raise SyntaxError(f"Неожиданный токен в массиве: {self.current_token}")
        if self.current_token[0] != 'RPAREN':
            raise SyntaxError("Ожидается ')' в конце массива")
        self.advance()
        return arr

    def parse_dict(self) -> dict:
        d = {}
        self.advance()  # пропускаем '{'
        while self.current_token and self.current_token[0] != 'RBRACE':
            if self.current_token[0] == 'CHAR':
                key = self.current_token[1]
                self.advance()
                if self.current_token[0] != 'ARROW':
                    raise SyntaxError("Ожидается '=>' после ключа")
                self.advance()
                value = self.parse()
                d[key] = value
                if self.current_token and self.current_token[0] == 'CHAR' and self.current_token[1] == ',':
                    self.advance()
            else:
                raise SyntaxError(f"Неожиданный токен в словаре: {self.current_token}")
        if self.current_token[0] != 'RBRACE':
            raise SyntaxError("Ожидается '}' в конце словаря")
        self.advance()
        return d
