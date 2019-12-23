#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        def hasPathSum_helper(root, s):
            nonlocal sum
            if (not root.left) and (not root.right):
                return s + root.val == sum

            return (root.left and hasPathSum_helper(root.left, s+root.val)) \
            or (root.right and hasPathSum_helper(root.right, s+root.val))
        
        return hasPathSum_helper(root, 0)
# @lc code=end

