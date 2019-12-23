#
# @lc app=leetcode id=188 lang=python3
#
# [188] Best Time to Buy and Sell Stock IV
#

# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        if k < len(prices) // 2:
            s = [-float("inf")] * (k * 2 + 1)
            s[0] = 0
            for price in prices:
                for i in range(k):
                    index = 2 * i
                    s[index + 1] = max(s[index + 1], s[index] - price)
                    s[index + 2] = max(s[index + 2], s[index + 1] + price)
            return max(s[-1], 0)
            
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

        

# @lc code=end

