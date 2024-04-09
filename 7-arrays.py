#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    # Reverse the array in place
    arr.reverse()

    # Print the reversed array elements as a single line
    new_array = map(str, arr)

    for i in new_array:
        print(i + " ", end="")
