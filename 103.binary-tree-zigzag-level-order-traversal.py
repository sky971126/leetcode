#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        self.zigzagLevelOrder_helper(root, 0, result)
        return result

    def zigzagLevelOrder_helper(self, node, depth, result):
        if node == None:
            return
        if len(result) == depth:
            result.append([])
        if depth % 2 == 0:
            result[depth].append(node.val)
        else:
            result[depth].insert(0, node.val)
        self.zigzagLevelOrder_helper(node.left, depth+1, result)
        self.zigzagLevelOrder_helper(node.right, depth+1, result)

