#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return not self.isValidBST_helper(root, -2 ** 31 - 1, 2 ** 31)

    def isValidBST_helper(self, node, mi, ma):
        if node == None:
            return False
        val = node.val
        if val <= mi or val >= ma:
            return True
        else:
            return self.isValidBST_helper(node.left, mi, min(ma, val)) + self.isValidBST_helper(node.right, max(mi, val), ma)

