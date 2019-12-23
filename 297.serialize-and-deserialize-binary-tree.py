#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return ""
        return str(root.val) + "," + self.serialize(root.left) + "," + self.serialize(root.right)

    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(",")[::-1]
        def deserialize_helper():
            val = data.pop()
            if not val: 
                return None
            val = int(val) 
            root = TreeNode(val)
            root.left = deserialize_helper()
            root.right = deserialize_helper()
            return root
        return deserialize_helper()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# @lc code=end

