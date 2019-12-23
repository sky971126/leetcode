#
# @lc app=leetcode id=706 lang=python3
#
# [706] Design HashMap
#

# @lc code=start

class Node:

    def __init__(self, key, value):
        self.pair = (key, value)
        self.next = None

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.k = 500
        self.map = [None] * self.k
        
    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        k = self.k
        map = self.map
        key_hash = key % k
        head = map[key_hash]
        while head:
            if head.pair[0] == key:
                head.pair = (key, value)
                return
            head = head.next
        head = map[key_hash]
        new = Node(key, value)
        new.next = head
        map[key_hash] = new

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        k = self.k
        map = self.map
        key_hash = key % k
        head = map[key_hash]
        while head:
            if head.pair[0] == key:
                return head.pair[1]
            head = head.next
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        k = self.k
        map = self.map
        key_hash = key % k
        head = map[key_hash]
        
        if head and head.pair[0] == key:
            map[key_hash] = head.next
            return
        
        while head and head.next:
            if head.next.pair[0] == key:
                head.next = head.next.next
                return 
            head = head.next

        

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end

