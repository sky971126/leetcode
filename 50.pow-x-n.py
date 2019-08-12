#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#
class Solution:
    def myPow(self, x, n):
        negative = False
        if n < 0:
            n = -n
            negative = True
        binary = bin(n)[2:]
        leng = len(binary)
        mul_list = [x]
        for i in range(1, leng):
            x = x * x
            mul_list.append(x)
        res = 1
        for i, c in enumerate(binary):
            if c == '1':
                res *= mul_list[leng - 1 - i]
        if negative:
            return 1 / res
        else:        
            return res

#print(Solution().myPow(2,-2))