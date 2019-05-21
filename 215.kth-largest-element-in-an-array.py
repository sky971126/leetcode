#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
class Solution:
    def findKthLargest(self, nums, k):
        n = len(nums)
        pivot = 0
        new_nums_l = []
        new_nums_r = []
        for i in range(n):
            new_nums_l = []
            new_nums_r = []
            for j in (nums[0:pivot] + nums[pivot+1:n]):
                if j < nums[pivot]:
                    new_nums_l.append(j)
                elif j > nums[pivot]:
                    new_nums_r.append(j)
            if (len(new_nums_r) < k) and (n - len(new_nums_l) + 1 > k):
                return nums[pivot]
            elif (len(new_nums_r) >= k):
                n = len(new_nums_r)
                nums = new_nums_r
            else:
                k = k - (n - len(new_nums_l))
                n = len(new_nums_l)
                nums = new_nums_l

# print(Solution().findKthLargest([-1,2,0],2))
        

