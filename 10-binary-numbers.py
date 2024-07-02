#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())

    binary_number = []

    # Convert input to binary number
    while n > 0:
        remainder = n % 2
        binary_number.append(remainder)

        # Update n with int result number
        n = n // 2

    consecutive_ones = 0
    max_number_consecutive_ones = 0

    # Check consecutive ones
    for i in range(len(binary_number)):
        # Check the begining of consecutive ones
        if binary_number[i] == 1:
            consecutive_ones += 1
            if consecutive_ones > max_number_consecutive_ones:
                max_number_consecutive_ones = consecutive_ones
        # Restart count of consecutive ones
        else:
            consecutive_ones = 0

    print(max_number_consecutive_ones)
