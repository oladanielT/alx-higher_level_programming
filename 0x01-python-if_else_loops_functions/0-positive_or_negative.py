#!/usr/bin/python3
"""
function to print number
"""
import random
number = random.randint(-10, 10)
if (number > 0):
    print("{} is positive".format(number))
elif (number == 0):
    print("{} is zero".format(number))
else:
    print("{} is negative".format(number))
