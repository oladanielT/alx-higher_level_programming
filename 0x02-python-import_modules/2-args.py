#!/usr/bin/python3
if __name__ == "__main__":
    """writing to make a script dynamic"""
    import sys


    arg_len = len(sys.argv) - 1
    print("{} arguement{}".format(arg_len, "s" if arg_len != 1 else ""), end="")

    if arg_len == 0:
        print(".")
    else:
        print(":")
        for i, arg in enumerate(sys.argv[1:], 1):
            print("{}: {}".format(i, arg))

