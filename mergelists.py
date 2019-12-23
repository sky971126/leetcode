class node:
    def __init__ (self, value):
        self.value = value
        self.next = None

def generate_test():    
    n1 = node(1)
    n2 = node(3)
    n3 = node(5)
    n1.next = n2
    n2.next = n3
    print(n1.value)
    print(n3.value)

    n4 = node(2)
    n5 = node(7)
    n4.next = n5
    
    n6 = node(4)

    return n1, n4, n6

def merge2(n1, n2):
    head = node(0)
    cur = head
    while n1 and n2:
        if n1.value < n2.value:
            cur.next = n1
            n1 = n1.next
            cur = cur.next
        else:
            cur.next = n2
            n2 = n2.next
            cur = cur.next
    if n1:
        cur.next = n1
    if n2:
        cur.next = n2

    return head.next

import math
def solution(lists):
    n = len(lists)
    while (n>1):
        new_lists = []
        for i in range(0,n,2): #0 2 4 6
            new_lists.append(merge2(lists[i], lists[i+1]))
        if n % 2 == 1: # 7
            new_lists.append(lists[-1])
        lists = new_lists
        n = math.ceil(n/2) 

    return new_lists[0]

n1, n4, n6 = generate_test()
merge2(n1, n4)