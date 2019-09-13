#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.levelOrder_helper(root, res, 0)
        return res

    def levelOrder_helper(self, node, res, level):
        if not node:
            return
        if level == len(res):
            res.append([])
        res[level].append(node.val)
        self.levelOrder_helper(node.left, res, level+1)
        self.levelOrder_helper(node.right, res, level+1)


