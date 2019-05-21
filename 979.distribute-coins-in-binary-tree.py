#
# @lc app=leetcode id=979 lang=python3
#
# [979] Distribute Coins in Binary Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distributeCoins(self, root):
        return self.distributeCoins_helper(root)[1]
    
    def distributeCoins_helper(self, node):
        if node == None:
            return 0, 0
        l, move_l = self.distributeCoins_helper(node.left)
        r, move_r = self.distributeCoins_helper(node.right)
        return l + r + node.val - 1, abs(l) + abs(r) + move_l + move_r
