#!/usr/bin/python3
"""Adding all arguments"""
if __name__ == "__main__":
    from sys import argv
    sum = 0
    for i in range(1, len(argv)):
        sum += int(argv[i])
    print(sum)
