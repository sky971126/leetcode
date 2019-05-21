#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x = str(x)
        n = len(x)
        for i in range(n//2):
            if x[i] != x[n-i-1]:
                return False
        return True
        

