#
# @lc app=leetcode id=491 lang=python3
#
# [491] Increasing Subsequences
#

# @lc code=start
class Solution:
    """
    def findSubsequences(self, nums):
        subs = {()}
        for num in nums:
            print(subs)
            subs |= {sub + (num,)
                    for sub in subs
                    if not sub or sub[-1] <= num}
        return [sub for sub in subs if len(sub) >= 2]
    """
    def findSubsequences(self, nums):
        if not nums:
            return []
        res = set()
        res.add((nums[0],))
        for num in nums[1:]:
            new_res = set()
            for seq in res:
                if seq[-1] <= num:
                    new_res.add(seq + (num,))
            res |= new_res
            res.add((num,))
        return [i for i in res if len(i) >= 2]
    
# @lc code=end

