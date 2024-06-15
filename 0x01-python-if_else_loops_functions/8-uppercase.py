#!/usr/bin/python3


def uppercase(str):
    for i in str:
        if (ord('a') <= ord(i) <= ord('z'):
                s = chr(ord(i) - 32)
        else:
            s = i
        print("{}".format(s), end="")
    print()
