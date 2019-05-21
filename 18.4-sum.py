#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#
class Solution:
    def fourSum(self, nums, target):
        results = []
        nums.sort()
        self.Nsum(nums, 4, target, [], results)
        return results
    
    def Nsum(self, nums, N, target, result, results):
        n = len(nums)
        if N == 2:
            self.twoSum(nums, target, result, results)
        else:
            for i in range(n-N+1):
                if target < N * nums[i] or target > N * nums[-1]:
                    break
                if i == 0 or i > 0 and nums[i-1] != nums[i]:
                    self.Nsum(nums[i+1:], N-1, target-nums[i], result+[nums[i]], results)
            
    def twoSum(self, nums, target, result, results):
        n = len(nums)
        l = 0
        r = n-1
        while l < r:
            sum = nums[l] + nums[r]
            if sum == target:
                results.append(result + [nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
                while l < r and nums[r] == nums[r+1]:
                    r -= 1
            elif sum < target:
                l += 1
            else:
                r -= 1
        return
                
#print(Solution().fourSum([1,0,-1,0,-2,2],0))

