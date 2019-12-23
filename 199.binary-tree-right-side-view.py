#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import queue
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        que = queue.Queue()
        que.put(root)
        res = []
        while not que.empty():
            que_new = queue.Queue()
            node = que.get()
            res.append(node.val)
            if node.right:
                que_new.put(node.right)
            if node.left:
                que_new.put(node.left)
            while not que.empty():
                node = que.get()
                if node.right:
                    que_new.put(node.right)
                if node.left:
                    que_new.put(node.left)
            que = que_new
        return res
# @lc code=end

