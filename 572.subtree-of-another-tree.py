#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        
        def check(s, t):
            if not t and not s:
                return True
            elif not t or not s or t.val != s.val:
                return False
            else:
                return check(s.left, t.left) and check(s.right, t.right)
        
        def traverse(s):
            if not s:
                return False
            if check(s,t):
                return True
            return traverse(s.left) or traverse(s.right)
        
        return traverse(s)

# @lc code=end