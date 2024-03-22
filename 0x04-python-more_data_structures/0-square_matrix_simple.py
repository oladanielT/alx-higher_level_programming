#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_row = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(element ** 2)
        squared_row.append(new_row)
    return squared_row
