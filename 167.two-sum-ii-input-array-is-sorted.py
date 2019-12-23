#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        D = {}
        for i in range(len(numbers)):
            num = numbers[i]
            if target - num in D:
                return [D[target-num]+1, i+1]
            D[num] = i
        return []

# @lc code=end

