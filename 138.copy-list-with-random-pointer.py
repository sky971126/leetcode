#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#
"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    """
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return None
        new_head = Node(head.val, None, None)
        h1 = head
        h2 = new_head
        d = {}
        d[h1] = h2
        h1 = h1.next
        while(h1!=None):
            new_node = Node(h1.val, None, None)
            d[h1] = new_node
            h2.next = new_node
            h2 = new_node
            h1 = h1.next
        for i in d:
            if i.random != None:
                d[i].random = d[i.random]
            else:
                d[i].random = None
        return new_head
    """









    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        h1 = head
        h2 = Node(head.val, None, None)
        d = {h1:h2}
        h1 = h1.next
        while h1:
            h2.next = Node(h1.val, None, None)
            h2 = h2.next
            d[h1] = h2
            h1 = h1.next
        h1 = head
        while h1:
            if h1.random:
                h2 = d[h1]
                h2_rand = d[h1.random]
                h2.random = h2_rand
            h1 = h1.next
        return d[head]







