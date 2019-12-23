# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
import queue

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        D = collections.defaultdict(list)
        que = queue.Queue()
        que.put((root, 0))
        while not que.empty():
            node, col = que.get()
            if not node:
                continue
            D[col].append(node.val)
            que.put((node.left, col-1))
            que.put((node.right, col+1))
        cols = list(D.keys())
        min_col = min(cols)
        max_col = max(cols)
        res = []
        for i in range(min_col, max_col+1):
            res.append(D[i])
        return res