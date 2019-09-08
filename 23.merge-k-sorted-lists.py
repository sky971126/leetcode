#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
import math
from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None
        while len(lists) > 1:
            new_lists = []
            for i in range(int(math.ceil(len(lists)/2))):
                new_lists.append(self.merge2Lists(lists[2*i:2*i+2]))
            lists = new_lists
        return lists[0]

    def merge2Lists(self, lists):
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        l1 = lists[0]
        l2 = lists[1]
        if not l1 and not l2:
            return None
        if not l1:
            start = l2
            l2 = l2.next
        elif not l2:
            start = l1
            l1 = l1.next
        else:
            if l1.val < l2.val:
                start = l1
                l1 = l1.next
            else:
                start = l2
                l2 = l2.next
        
        move = start
        while l1 or l2:
            if not l1 and not l2:
                return None
            if not l1:
                move.next = l2
                l2 = l2.next
            elif not l2:
                move.next = l1
                l1 = l1.next
            else:
                if l1.val < l2.val:
                    move.next = l1
                    l1 = l1.next
                else:
                    move.next = l2
                    l2 = l2.next
            move = move.next
        return start


    #priority queue
    """
    def mergeKLists(self, lists):
        class Wrapper():
            def __init__(self, node):
                self.node = node
            def __lt__(self, other):
                return self.node.val < other.node.val
        
        q = PriorityQueue()
        for node in lists:
            if node:
                q.put(Wrapper(node))

        if q.empty():
            return None 

        head = q.get(block=True).node
        
        move = head
        while not q.empty():
            if move.next:
                q.put(Wrapper(move.next))
            move.next = q.get(block=True).node
            move = move.next
            
        return head
    """
