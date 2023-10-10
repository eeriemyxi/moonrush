from enum import Enum, auto
from dataclasses import dataclass


class TokenType(Enum):
    IDENTIFIER = auto()
    STRING = auto()

    EOF = auto()


@dataclass
class Token:
    token_type: TokenType
    lexeme: object
    line: int
