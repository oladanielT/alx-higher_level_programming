#!/usr/bin/python3
if __name__ == "__main__":
    """script to print the args"""
    arg_ = len(argv)
    print("{} argument{}".format(arg_, "s" if arg_ != 1 else ""), end="")
    if arg_ == 0:
        print(".")
    else:
        print(":")
        for i, arg in enumerate(sys.arg[1:], 1):
            print("{}: {}".format(i, arg))
