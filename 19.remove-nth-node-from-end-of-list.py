#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
# Definition for singly-linked list.
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""

#optimize two pointers with distance n
class Solution:
    def removeNthFromEnd(self, head, n):
        stack = []
        mov = head
        while mov != None:
            stack.append(mov)
            mov = mov.next
        N = len(stack)
        if N-n-1 >= 0:
            stack[N-n-1].next = stack[N-n].next
        else:
            head = stack[N-n].next
        return head
"""
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
nh = Solution().removeNthFromEnd(n1,5)
"""