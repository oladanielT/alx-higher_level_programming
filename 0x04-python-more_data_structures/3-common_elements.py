#!/usr/bin/python3
def common_elements(set_1, set_2):
    if set_1 and set_2:
        for i in set_1:
            for j in set_2:
                if i == j:
                    return i
                else:
                    return None
    else:
        return
