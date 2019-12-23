#
# @lc app=leetcode id=714 lang=python3
#
# [714] Best Time to Buy and Sell Stock with Transaction Fee
#
class Solution:
    """
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0
        cash = 0
        hold = -prices[0]
        for price in prices[1:]:
            cash = max(cash, hold+price-fee)
            hold = max(cash-price, hold)
        return cash
    
    """


    def maxProfit(self, prices: List[int], fee: int) -> int:
        if len(prices) < 2:
            return 0
        hold = -prices[0] - fee
        cash = 0
        for price in prices[1:]:
            new_hold = max(hold, cash - price - fee)
            new_cash = max(cash, hold + price)
            hold, cash = new_hold, new_cash
        return cash


