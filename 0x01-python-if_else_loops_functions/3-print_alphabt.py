#!/usr/bin/python3

for item in range(97, 123):
    if (item == ord('q') or item == ord('e')):
        continue
    print("{}".format(chr(item)), end='')
