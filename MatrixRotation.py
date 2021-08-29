#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'matrixRotation' function below.
#
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY matrix
#  2. INTEGER r
#
def rotate(i, j, r, m, n):
    if (m <= n):
        mid = m / 2 - 1 if m % 2 == 0 else int(m / 2) + 1
        d1 = i if i <= mid else m - i - 1
        d2 = n - d1 - 1
        if j >= d1 and j <= d2:
            block = d1
        elif j < d1:
            block = j
        elif j > d2:
            block = n - j - 1
    else:
        mid = n / 2 - 1 if n % 2 == 0 else int(n / 2) + 1
        d1 = j if j <= mid else n - j - 1
        d2 = m - d1 - 1
        if i >= d1 and i <= d2:
            block = d1
        elif i < d1:
            block = i
        elif i > d2:
            block = m - i - 1
    minRow = block
    maxRow = m - block - 1
    minCol = block
    maxCol = n - block - 1

    s1 = 2 * (maxRow - minRow) + 2 * (maxCol - minCol)
    r = r % s1
    while (r > 0):
        if r > 0 and i == minRow:
            diff = maxCol - j
            if diff >= r:
                j += r
                r = 0
            else:
                j = maxCol
                r -= diff
        if r > 0 and i == maxRow:
            diff = j - minCol
            if diff >= r:
                j -= r
                r = 0
            else:
                j = minCol
                r -= diff
        if r > 0 and j == minCol:
            diff = i - minRow
            if diff >= r:
                i -= r
                r = 0
            else:
                i = minRow
                r -= diff
        if r > 0 and j == maxCol:
            diff = maxRow - i
            if diff >= r:
                i += r
                r = 0
            else:
                i = maxRow
                r -= diff
    return i, j


def matrixRotation(matrix, r):
    m = len(matrix)
    n = len(matrix[0])

    for i in range(m):
        for j in range(n):
            iR, jR = rotate(i, j, r, m, n)
            print(str(matrix[iR][jR]) + " ", end="")
        print("")


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    r = int(first_multiple_input[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
