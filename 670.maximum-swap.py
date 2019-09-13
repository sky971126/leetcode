#
# @lc app=leetcode id=670 lang=python3
#
# [670] Maximum Swap
#
import math
class Solution:
    def maximumSwap(self, num: int) -> int:
        if num <= 10:
            return num
        num_str = str(num)
        decrease = [int(num_str[0])]
        swap = False
        for i in range(1, len(num_str)):
            d = int(num_str[i])
            if d <= decrease[-1]:
                decrease.append(d)
            else:
                swap = True
                break
        if not swap:
            return num
        d_max = int(num_str[i])
        index_max = i
        for j in range(i+1, len(num_str)):
            d = int(num_str[j])
            if d >= d_max:
                d_max = d
                index_max = j

        for j in range(i):
            d = int(num_str[j])
            if d < d_max:
                index_left_most = j
                break
        
        num_str = num_str[0:index_left_most] + num_str[index_max] +\
            num_str[index_left_most+1:index_max] + num_str[index_left_most] +\
            num_str[index_max+1:]
        return int(num_str)


