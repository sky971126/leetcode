#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        res = 0
        low = prices[0]
        for i, price in enumerate(prices[1:]):
            if price < prices[i]:
                res += max(prices[i] - low, 0)
                low = price
        res += max(prices[-1] - low, 0)
        return res


    