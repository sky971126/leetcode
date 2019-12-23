#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res_list = []
        candidates.sort()
        def combinationSum2_helper(target, res, index):
            if target < 0:
                return
            if target == 0:
                res_list.append(tuple(res))
                return
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                combinationSum2_helper(target-candidates[i], res + [candidates[i]], i+1)
            return
        combinationSum2_helper(target, [], 0)
        return res_list
# @lc code=end

