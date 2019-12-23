#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        count = 0
        def pathSum_helper(root, sum_list):
            nonlocal count
            nonlocal sum
            if not root:
                return
            if root.val == sum:
                count += 1
            new_list = [root.val]
            for s in sum_list:
                if s + root.val == sum:
                    count += 1
                new_list.append(s+root.val)
            pathSum_helper(root.left, new_list)
            pathSum_helper(root.right, new_list)

        
        pathSum_helper(root, [])
        return count

            
# @lc code=end

