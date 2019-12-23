#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
import collections
import random
class Solution:
    def topKFrequent(self, nums, k: int):
        #return [i[0] for i in sorted(collections.Counter(nums).items(), key=lambda x: -x[1])[:k]]
        ct = collections.Counter(nums)
        nums = list(ct.keys())
        def partition(i, j):
            l, r = i+1, j
            while True:
                while l <= j and ct[nums[l]] > ct[nums[i]]:
                    l += 1
                while r >= i+1 and ct[nums[r]] <= ct[nums[i]]:
                    r -= 1
                if l < r:
                    nums[l], nums[r] = nums[r], nums[l]
                else:
                    break
            nums[i], nums[r] = nums[r], nums[i]
            return r

        def sortk(i, j, k):
            pivot = random.randint(i, j)
            nums[i], nums[pivot] = nums[pivot], nums[i]
            mid = partition(i, j)
            if mid > k:
                sortk(i, mid - 1, k)
            elif mid < k-1:
                sortk(mid + 1, j, k)

        sortk(0, len(nums)-1, k)
        return nums[:k]

# @lc code=end

print(Solution().topKFrequent([3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6], 10))