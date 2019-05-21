#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
class Solution:
    def combinationSum(self, candidates, target):
        n = len(candidates)
        candidates.sort()
        results = []
        self.combinationSum_helper(candidates, n, target, [], results)
        return results

    def combinationSum_helper(self, candidates, length, target, result, results):
        if target == 0:
            results.append(result)
            return
        if target < candidates[0]:
            return
        for i in range(length):
            self.combinationSum_helper(candidates, i+1, target-candidates[i], [candidates[i]] + result, results)
        return

#print(Solution().combinationSum([2,3,6,7],7))