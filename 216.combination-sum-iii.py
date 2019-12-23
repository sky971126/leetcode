#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res_list = []
        
        def combinationSum3_helper(k, n, res, index):
            if k == 0:
                if n == 0:
                    res_list.append(res)
                return
            if n <= 0:
                return
            for i in range(index, 10):
                combinationSum3_helper(k-1, n-i, res + [i], i+1)
        combinationSum3_helper(k, n, [], 1)
        return res_list


                 
# @lc code=end

