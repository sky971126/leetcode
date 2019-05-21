#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#
class Solution:
    def coinChange(self, coins, amount):
        n = len(coins)
        #coins.sort(reverse = True)
        return self.coinChange_helper(coins, amount, {})
        
    def coinChange_helper(self, coins, amount, dic):
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        if amount in dic:
            return dic[amount]
        min_num = -1
        for i in range(len(coins)):
            num_i = self.coinChange_helper(coins, amount-coins[i], dic)
            if num_i >= 0:
                if min_num == -1:
                    min_num = num_i + 1
                else:
                    min_num = min(min_num, num_i + 1)
        dic[amount] = min_num
        return min_num
#print(Solution().coinChange([186,419,83,408],6249))