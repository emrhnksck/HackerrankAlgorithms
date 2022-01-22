#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    alice_point = 0
    bob_point = 0
    for i in range(3):
        if a[i] > b[i]:
            alice_point+=1
        if a[i] < b[i]:
            bob_point+=1
    return [alice_point,bob_point]

print(compareTriplets([5,6,7],[3,6,10]))