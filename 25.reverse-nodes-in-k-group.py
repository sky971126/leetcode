#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        move = head
        cont, last, next_move = self.remainK(move, k)
        if cont:
            head = last
        while cont:
            head_k = move
            nex = move.next
            for i in range(k-1):
                nex_nex = nex.next
                nex.next = move
                move = nex
                nex = nex_nex
            move = next_move
            cont, last, next_move = self.remainK(move, k)
            if cont:
                head_k.next = last
            else:
                head_k.next = next_move
        return head
    
    def remainK(self, head, k):
        move = head
        for i in range(k):
            if not move:
                return False, None, head
            if i == k-1:
                last = move
            move = move.next
        return True, last, move

