#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#
def climbingLeaderboard(ranked, player):

    i = 0
    length_ranked = len(ranked)
    k = length_ranked - 1
    counter = 0
    rank = len(set(ranked)) + 1
    while counter < len(player):

        if i >= len(player):
            print('Error')
            break
        if k < 0:
            yield rank
            k = length_ranked - 1
            i += 1
            counter += 1
            continue
        if player[i] < ranked[k]:
            yield rank
            counter += 1
            i += 1
        else:
            k -= 1
            while k >= 0 and ranked[k] == ranked[k + 1]:
                k -= 1
            rank = rank - 1 if rank > 1 else 1
        

                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()