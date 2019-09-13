#
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change 2
#
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if not coins:
            if amount == 0:
                return 1
            else:
                return 0
        DP = [0] * (amount + 1)
        DP[0] = 1
        for coin in coins:
            for i in range(coin, amount+1):
                DP[i] += DP[i-coin]
        return DP[amount]

    ### No need for 2-D DP
    """
    def change(self, amount: int, coins: List[int]) -> int:
        DP = {}
        return self.change_helper(amount, coins, 0, DP)
        # (amount, index) : num

    def change_helper(self, amount, coins, index, DP): # 0<=index<=len(coins)-1
        if amount < 0:
            return 0
        if amount == 0:
            return 1
        if (amount, index) not in DP:
            DP[(amount, index)] = 0
            for i in range(index, len(coins)):
                DP[(amount, index)] += self.change_helper(amount - coins[i], coins, i, DP)
        return DP[(amount, index)]
    """
