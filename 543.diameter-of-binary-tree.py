#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        if not root:
            return 0
        return max(self.helper(root)) - 1
    
    def helper(self, root):
        if root == None:
            return [0,0]
        l = self.helper(root.left)
        r = self.helper(root.right)
        return [max(l[0],r[0]) + 1, max((l[0] + r[0] +1), l[1], r[1])]
"""
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)

t1.left = t2
t1.right = t3
t2.left = t4
t2.right = t5
print(Solution().diameterOfBinaryTree(t1))
"""
        

