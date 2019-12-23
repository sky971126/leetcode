#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        move = head
        nex = move.next
        move.next = None
        while (nex):
            new_nex = nex.next
            nex.next = move
            move = nex
            nex = new_nex
        return move
# @lc code=end

