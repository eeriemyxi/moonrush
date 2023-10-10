from moonrush.structs.tokens import Token, TokenType


class Scanner:
    def __init__(self, source: str):
        self.source = source

        self.tokens = []

        self._t_start = 0
        self.current = 0
        self.line = 1

    def is_at_end(self):
        return self.current >= len(self.source)

    def advance(self):
        cur_char = self.source[self.current]
        self.current += 1
        return cur_char

    def peek(self):
        return "" if self.is_at_end() else self.source[self.current]

    def handle_string(self):
        while self.peek() != '"' and not self.is_at_end():
            if self.peek() == "\n":
                self.line += 1
            self.advance()

        if self.is_at_end():
            raise Exception
        else:
            self.advance()

        string_value = self.source[self._t_start + 1:self.current - 1]
        self.tokens.append(Token(TokenType.STRING, string_value, self.line))
    
    def handle_number(self):
        ...

    def handle_identifier(self):
        ...

    def scan_tokens(self) -> list[Token]:
        while not self.is_at_end():
            self._t_start = self.current
            self.scan_token()

        self.tokens.append(Token(token_type=TokenType.EOF, lexeme="", line=self.line))

        return self.tokens

    def scan_token(self):
        char = self.advance()
        match char:
            case '"':
                self.handle_string()
            case " " | "\t":
                pass
            case "\n":
                self.line += 1
            case _:
                if char.isdigit():
                    self.handle_number()
                elif char.isalpha():
                    self.handle_identifier()
                else:
                    raise Exception
