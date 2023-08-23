#!/usr/bin/python3
# by - musonda christopher
# A Python function that prints a matrix of integers.
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col in row:
            print("{:d}".format(col), end=" " if col != row[-1] else "")
        print()
