#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # res = []
        # for debug
        # def printTree(root):
        #     if not root:
        #         res.append(None)
        #     else:
        #         res.append(root.val)
        #         printTree(root.left)
        #         printTree(root.right)

        def maxPathSum_helper(root):
            if not root:
                return 0, -float("inf")
            path_sum_l, total_sum_l = maxPathSum_helper(root.left)
            path_sum_r, total_sum_r = maxPathSum_helper(root.right)
            # 0 !
            path_sum = max(path_sum_l, path_sum_r, 0) + root.val
            total = root.val
            if path_sum_l > 0:
                total += path_sum_l
            if path_sum_r > 0:
                total += path_sum_r
            total_sum = max(total_sum_l, total_sum_r, total)
            return path_sum, total_sum
        
        # if root.val == 9:
        #     printTree(root)
        #     print(res)

        return max(maxPathSum_helper(root))
# @lc code=end
