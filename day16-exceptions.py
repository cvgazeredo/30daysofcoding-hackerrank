#!/bin/python3

import math
import os
import random
import re
import sys

# In this challenge is necessary to remove the the following line
# "if __name__ == '__main__':"


S = input()

try:
    print(int(S))

except:
    print("Bad String")
