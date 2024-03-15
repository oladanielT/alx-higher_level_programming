#!/usr/bin/python3
if __name__ == "__main__":
    """script to print the args"""
    from sys import argv
    x = len(argv) - 1
    print("{}: argument{:s}".format(x, "s" if x != 1 else ""), end="")
    if x == 0:
        print(".")
    else:
        print(":")
        for i in range(x):
            print("{}: {:s}".format(i + 1, argv[i + 1]))
