#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
#
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        roots = []
        self.connect_helper(root, roots, 0)
        return root
    
    def connect_helper(self, node, roots, level):
        if not node:
            return
        if len(roots) == level:
            roots.append(node)
        else:
            roots[level].next = node
            roots[level] = node
        self.connect_helper(node.left, roots, level+1)
        self.connect_helper(node.right, roots, level+1)

