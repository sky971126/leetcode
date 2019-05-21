#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#
class Solution:
    def permuteUnique(self, nums):
        results = []
        nums.sort()
        self.permuteUnique_helper(nums, [], results)
        return results

    def permuteUnique_helper(self, nums, result, results):
        if not nums:
            results.append(result)
            return
        for i in range(len(nums)):
            if i>=1 and nums[i] == nums[i-1]:
                continue
            self.permuteUnique_helper(nums[:i]+nums[i+1:], result+[nums[i]], results)
    
    #keep inserting
    """
    def permuteUnique(self, nums):
        ans = [[]]
        for n in nums:
            new_ans = []
            for l in ans:
                for i in range(len(l)+1):
                    new_ans.append(l[:i]+[n]+l[i:])
                    if i<len(l) and l[i]==n: break              #handles duplication
            ans = new_ans
        return ans
    """
#print(Solution().permuteUnique([1,2,2]))