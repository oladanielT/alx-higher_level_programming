#!/usr/bin/python3


for i in range(ord('Z'), ord('A') - 1, - 1):
    a = chr(i + 32) if i % 2 == 0 else chr(i)
    print("{}".format(a), end='')
