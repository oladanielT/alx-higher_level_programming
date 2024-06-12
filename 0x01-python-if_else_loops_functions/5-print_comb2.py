#!/usr/bin/python3

for item in range(100):
    size = 0 if item < 10 else ''

    print("{}{}".format(size, item), end= ', ' if item < 99 else '')
print()
