#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
class Solution:
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

