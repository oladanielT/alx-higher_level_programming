#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        length = 0
        first_c = None
        return length, first_c
    else:
        length = len(sentence)
        first_c = sentence[0]
        return length, first_c
