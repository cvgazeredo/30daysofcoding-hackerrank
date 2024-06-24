#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    # Reverse the array 
    arr.reverse()

    # Convert each integer element to string
    new_array = map(str, arr)

    # Print each element separated by space
    for element in new_array:
        print(element + " ", end="")
