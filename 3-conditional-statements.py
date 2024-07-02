#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    N = int(input().strip())

    # If  is odd, print Weird
    if (N % 2 != 0):
        print("Weird")
    # If is even:
    else:
        # .. and in the inclusive range of 2 to 5, print Not Weird
        if N >= 2 and N <= 5:
            print("Not Weird")
        # .. and in the inclusive range of 6 to 20, print Weird
        elif N >= 6 and N <= 20:
            print("Weird")
        # .. and greater than 20, print Not Weird
        elif N > 20 and N <= 100:
            print("Not Weird")
            
