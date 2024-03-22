#!/usr/bin/python3
def common_elements(set_1, set_2):
    for first in set_1:
        for sec in set_2:
            if first == sec:
                return first
            else:
                return
