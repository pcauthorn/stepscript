from dataclasses import dataclass
from typing import Dict

class Test:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f'Data: {self.a}, {self.b}, {self.c}'


@dataclass
class TestDataClass:
    test: str
    test_int: int
    test_dict: Dict
