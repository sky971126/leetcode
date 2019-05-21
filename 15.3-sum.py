#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
class Solution:
    def threeSum(self, nums):
        n = len(nums)
        if n < 3:
            return []
        results = set()
        nums.sort()
        for i in range(n-2):
            if nums[i] > 0:
                break          
            if (i > 0) and (nums[i] == nums[i-1]):
                continue
            complement = {}
            for j in range(i+1,n):
                if nums[j] in complement:
                    results.add((nums[i], nums[j], -nums[i]-nums[j]))
                else:
                    complement[-nums[i] - nums[j]] = 0

        return [list(i) for i in results]
        

#print(Solution().threeSum([0,0,0]))