#!/usr/bin/python3
from sys import argv
import calculator_1
if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]
    if op == "+":
        print(f"{a} op {b} = {calculator_1.add(a, b)}")
    elif op == "":
        print(f"{a} op {b} = {calculator_1.sub(a, b)}")
    elif op == "":
        print(f"{a} op {b} = {calculator_1.mul(a, b)}")
    elif op == "":
        print(f"{a} op {b} = {calculator_1.div(a, b)}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
