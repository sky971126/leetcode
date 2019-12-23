#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        res_list = []
        def pathSum_helper(root, res, s):
            nonlocal sum
            if not root.left and not root.right and root.val + s == sum:
                res_list.append(res + [root.val])
                return
            if root.left:
                pathSum_helper(root.left, res+[root.val], s+root.val)
            if root.right:
                pathSum_helper(root.right, res+[root.val], s+root.val)
        pathSum_helper(root, [], 0)
        return res_list
            

# @lc code=end

