#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
import random
class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        max_flag = True
        n = len(nums)
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                max_flag = False
                break
        # to replace i-1
        if max_flag:
            nums.reverse()
            return
        j = 0
        if nums[-1] > nums[i-1]:
            j = n
        else:
            for j in range(i, n):
                if nums[j] <= nums[i-1]:
                    break
        # to replace j-1
        tmp = nums[j-1]
        nums[j-1] = nums[i-1]
        nums[i-1] = tmp

        for j in range((n-i)//2):
            tmp = nums[i+j]
            nums[i+j] = nums[n-1-j]
            nums[n-1-j] = tmp

        #sort i to n-1
        #actually no need to sort reverse the latter part is enough
        """
        def partition(i, j):
            l, r = i+1, j
            p = nums[i]
            while 1:
                while l <= j and nums[l] < p:
                    l += 1
                while r >= i+1 and nums[r] >= p:
                    r -= 1
                if l > r:
                    break
                else:
                    tmp = nums[l]
                    nums[l] = nums[r]
                    nums[r] = tmp
            nums[i] = nums[r]
            nums[r] = p
            return r

        def sort(i, j):
            if i >= j:
                return
            index = random.randint(i, j)
            tmp = nums[i]
            nums[i] = nums[index]
            nums[index] = tmp            
            m = partition(i, j)
            sort(i, m-1)
            sort(m+1, j)

        sort(i, n-1)
        """

# @lc code=end
Solution().nextPermutation([2,2,7,5,4,3,2,2,1])