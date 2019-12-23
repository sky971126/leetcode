#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head = l1
        l1_reserve = None
        while (l1 or l2):
            sum = carry
            if l1:
                sum += l1.val
            if l2:
                sum += l2.val
            carry = sum // 10
            if not l1:
                l1 = l2
                if l1_reserve:
                    l1_reserve.next = l1
                l2 = None
            l1.val = sum % 10
            if l1.next == None:
                l1_reserve = l1
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry:
            l1_reserve.next = ListNode(1)

        return head

