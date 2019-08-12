#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#
class Solution:
    def canPartition(self, nums):
        n = len(nums)
        s = sum(nums)
        if not nums:
            return False
        if s % 2 == 1:
            return False
        half = int(s / 2)
        sums = set([0])
        for num in nums:
            if num == half:
                return True
            add_list = []
            for i in sums:
                if i + num == half:
                    return True
                if i + num not in sums and i + num < half:
                    add_list.append(i + num)
            for i in add_list:
                sums.add(i)
        return False
    
    """ recursive TLE
    def canPartition(self, nums):
        n = len(nums)
        s = sum(nums)
        if not nums:
            return False
        if s % 2 == 1:
            return False
        half = s / 2
        return self.canPartition_helper(nums, 0, half)

    def canPartition_helper(self, nums, start, remain):
        if remain < 0:
            return False
        if remain == 0:
            return True
        for i in range(start, len(nums)):
            if self.canPartition_helper(nums, i+1, remain-nums[i]):
                return True
        return False 
    """
#Solution().canPartition([1,5,11,5])


