#!/usr/bin/python3


def uppercase(str):
    for i in str:
        g = ord(i) >= ord('a')
        lw = ord(i) <= ord('z')
        s = chr(ord(i) - 32) if g and lw else i
        print("{}".format(s), end="")
