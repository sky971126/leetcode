#
# @lc app=leetcode id=508 lang=python3
#
# [508] Most Frequent Subtree Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        S = collections.defaultdict(int)
        def findFrequentTreeSum_helper(root):
            if not root:
                return 0
            s = root.val
            s += findFrequentTreeSum_helper(root.left)
            s += findFrequentTreeSum_helper(root.right)
            S[s] += 1
            return s
        findFrequentTreeSum_helper(root)
        max_val = 0
        res = []
        for key, val in S.items():
            if max_val == val:
                res.append(key)
            elif max_val < val:
                res = [key]
                max_val = val
        return res

# @lc code=end