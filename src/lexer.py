from typing import List, Tuple

Token = Tuple[str, str]  # тип, значение

class Lexer:
    def __init__(self, text: str):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos] if self.text else None

    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def generate_tokens(self) -> List[Token]:
        tokens = []
        while self.current_char is not None:
            if self.current_char.isdigit():
                tokens.append(('NUMBER', self.number()))
            elif self.current_char in " \t\n":
                self.advance()
            else:
                tokens.append(('CHAR', self.current_char))
                self.advance()
        return tokens

    def number(self) -> str:
        num_str = ''
        while self.current_char is not None and self.current_char.isdigit():
            num_str += self.current_char
            self.advance()
        return num_str
