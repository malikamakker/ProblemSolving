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
def binarySearch(ranks, score):
    low = 0
    high = len(ranks) - 1

    while low <= high:
        mid = int((low + high) / 2)

        if mid < (len(ranks) - 1) and score <= ranks[mid] and score > ranks[mid + 1]:
            break
        if mid == (len(ranks) - 1) and score <= ranks[mid]:
            break
        if mid == 0 and score >= ranks[mid]:
            break

        if score > ranks[mid]:
            high = mid - 1
        if score <= ranks[mid]:
            low = mid + 1
    if mid == 0 and ranks[mid] < score:
        ranks.insert(mid, score)
        return mid + 1
    if ranks[mid] != score:
        ranks.insert(mid + 1, score)
        return mid + 2
    return mid + 1


def climbingLeaderboard(ranked, player):
    # remove duplicates
    ranks = [ranked[0]]
    result = []
    for rank in ranked[1:]:
        if rank != ranks[-1]:
            ranks.append(rank)

    for score in player:
        result.append(binarySearch(ranks, score))

    return result


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
