#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

ld = number % 10
s = "-" if number < 0 else "" if number == 0 else ""

if (ld == 0):
    print(f"Last digit of {number} is {ld} and is 0")
if (ld < 6 or ld != 0):
    print(f"Last digit of {number} is {s}{ld} and is less than 6 and not 0")
elif (ld > 5):
    print(f"Last digit of {number} is {s}{ld} and is greater than 5")
