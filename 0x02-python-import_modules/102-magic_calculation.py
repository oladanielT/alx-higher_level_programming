#!/usr/bin/python3
from magic_calculation_102 import a, b
def magic_calculation(a, b):
    if a < b:
        c = a + b
        for i in range(4, 6):
            c += i
        return c
    else:
        return a - b
