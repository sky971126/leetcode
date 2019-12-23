#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums) -> int:
        fast = 0
        slow = 0
        while 1:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
        slow1 = slow
        slow2 = 0
        while slow1 != slow2:
            slow1 = nums[slow1]
            slow2 = nums[slow2]
        return slow1
# @lc code=end

Solution().findDuplicate([1,3,4,2,2])