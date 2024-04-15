#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    max_sum_of_hourglasses = float('-inf')

    for i in range(6):
        if i <= 3:
            for j in range(6):
                if j <= 3:
                    sum_of_hourglass = sum(
                        arr[i][j:j+3]) + arr[i + 1][j + 1] + sum(arr[i + 2][j:j+3])

                    if sum_of_hourglass > max_sum_of_hourglasses:
                        max_sum_of_hourglasses = sum_of_hourglass

    print(max_sum_of_hourglasses)
