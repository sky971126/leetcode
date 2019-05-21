#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
class Solution:
    def maxSubArray(self, nums):
        n = len(nums)
        max_sum = nums[0]
        mov_sum = nums[0]
        for i in range(1,n):
            if mov_sum < 0:
                if nums[i] > mov_sum:
                    mov_sum = nums[i]
                    max_sum = max(max_sum, mov_sum)
                else:
                    max_sum = max(max_sum, mov_sum)
                    if i != n-1:
                        mov_sum = 0
            else:
                mov_sum += nums[i]
                max_sum = max(max_sum, mov_sum)
        max_sum = max(max_sum, mov_sum)
        return max_sum
            

    def maxSubArray_helper(self, nums, left):
        n = len(nums)
        if n == 0:
            return 0, 0
        if n == 1:
            return nums[0], nums[0]
        concat_l, max_l= self.maxSubArray(nums[:n//2], True)
        concat_r, max_r = self.maxSubArray(nums[n//2:], False)

#print(Solution().maxSubArray([-1,0,-2]))