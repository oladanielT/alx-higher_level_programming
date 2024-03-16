#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    res = dir()
    for i in range(0, len(res)):
        if res[i][:2] != "__":
            print("{:s}".format(res[i]))
