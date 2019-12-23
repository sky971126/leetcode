#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        slow = head
        fast = head
        while (True):
            if not fast:
                return None
            slow = slow.next
            fast = fast.next
            if not fast:
                return None
            fast = fast.next
            if fast == slow:
                break
        
        while (slow != head):
            slow = slow.next
            head = head.next
        return slow
# @lc code=end

# n1 = ListNode(1)
# n2 = ListNode(2)
# n3 = ListNode(3)
# n4 = ListNode(4)
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n2

# print(Solution().detectCycle(n1).val)