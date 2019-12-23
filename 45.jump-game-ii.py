#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums) -> int:
        """ DP ways
        n = len(nums)
        if n < 2:
            return 0
        dp = [float("inf")] * n
        dp[n-1] = 0
        for i in range(n-2, -1, -1):
            for j in range(1, nums[i]+1):
                if i + j < n:
                    dp[i] = min(dp[i], dp[i+j] + 1)
                else:
                    break
        return dp[0]
        """
        if len(nums) < 2:
            return 0
        res = 1
        l, r = 0, nums[0]
        while r < len(nums) - 1:
            res += 1
            next = max(i + nums[i] for i in range(l, r+1))
            l, r = r, next
            if l == r:
                return -1
        return res

# @lc code=end

print(Solution().jump([3,2,1,3,1,1,1,5,1]))

