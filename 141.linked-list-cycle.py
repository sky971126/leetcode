#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        slow = head
        fast = head.next
        while(slow != fast):
            if not fast:
                return False
            slow = slow.next
            fast = fast.next
            if not fast:
                return False
            fast = fast.next
        return True
        

# @lc code=end

