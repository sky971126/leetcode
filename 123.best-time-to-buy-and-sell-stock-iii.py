#
# @lc app=leetcode id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#

# @lc code=start
import heapq
class Solution:
    # Two Peak-Valley ways Wrong
    """
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        res = [0, 0]
        low = prices[0]
        for i, price in enumerate(prices[1:]):
            if price < prices[i]:
                diff = max(prices[i] - low, 0)
                if len(res) < 2:
                    heapq.heappush(diff)
                elif res[0] < diff:
                    heapq.heappop(res)
                    heapq.heappush(res, diff)
                low = price
        diff = max(prices[-1] - low, 0)
        if len(res) < 2:
            heapq.heappush(diff)
        elif res[0] < diff:
            heapq.heappop(res)
            heapq.heappush(res, diff)
        return sum(res)
    """
    def maxProfit(self, prices: List[int]) -> int:
        s1 = s2 = s3 = s4 = -float("inf")
        for price in prices:
            s1 = max(s1, 0 - price)
            s2 = max(s2, s1 + price)
            s3 = max(s3, s2 - price)
            s4 = max(s4, s3 + price)
        return max(s4, 0)

# @lc code=end

