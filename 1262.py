class Solution:
    def maxSumDivThree(self, nums) -> int:
        dp = [0] * 3
        for i in nums:
            dp_tmp = dp.copy()
            for j in dp_tmp:
                dp[(i+j)%3] = max(dp[(i+j)%3], i+j)
        return dp[0]

print(Solution().maxSumDivThree([3,6,5,1,8]))