#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'longestChain' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY words as parameter.
#
import collections
def longestChain(words):
    # Write your code here
    D = collections.defaultdict(set)
    max_len = 0
    for i in words:
        D[len(i)].add(i)
        max_len = max(max_len, len(i))
    
    def dfs(word):
        max_len = 1
        for i in range(len(word)):
            trim = word[:i] + word[i+1:]
            if trim in words: 
                max_len = max(max_len, 1 + dfs(trim))
        return max_len

    res = 1
    for i in range(max_len,0,-1):
        for word in D[i]:
            res = max(res, dfs(word))
    return res
            


print(longestChain(["a", "an", "and", "bear"]))