#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        

        def buildTree_helper(preorder, inorder):
            if not preorder:
                return None
            root_val = preorder[0]
            root = TreeNode(root_val)
            index = inorder.index(root_val)
            inorder_left = inorder[:index]
            inorder_right = inorder[index+1:]
            preorder_left = preorder[1:1+index]
            preorder_right = preorder[1+index:]
            root.left = buildTree_helper(preorder_left, inorder_left)
            root.right = buildTree_helper(preorder_right, inorder_right)
            return root
        
        return buildTree_helper(preorder, inorder)



# @lc code=end

