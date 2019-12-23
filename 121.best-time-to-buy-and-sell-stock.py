#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
class Solution:
    # good but long
    
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        res = 0
        min_p = prices[0]
        max_p = prices[0]
        for price in prices:
            if price > max_p:
                max_p = price
                res = max(res, max_p - min_p)
            if price < min_p:
                min_p = price
                max_p = -1
        return res
    """
    def maxProfit(self, prices: List[int]) -> int:
        s1 = s2 = -float("inf")
        for price in prices:
            s1 = max(s1, -price)
            s2 = max(s2, s1 + price)
        return max(s2, 0)
    """
