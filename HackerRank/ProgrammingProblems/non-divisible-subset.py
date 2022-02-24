#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#
def nonDivisibleSubset(k, s):
    count = 0
    vals = {(x):[] for x in range(0,k)}
    for x in s:
        vals[x % k].append(x)
    
    if len(vals[0]) > 0:
        count += 1
    
    for i in range(1,k // 2 + 1):
        if i == k - i and len(vals[i]) > 0:
            count += 1
        else:
            count += max(len(vals[i]), len(vals[k - i]))

    return count
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
