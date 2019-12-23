#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#
"""
class LRUCache:

    def __init__(self, capacity: int):
        from collections import OrderedDict
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key, last=True)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key, last=True)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
        

"""



import collections
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key, last=True)
            return self.cache[key]
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = value
        else:
            if len(self.cache) < self.capacity:
                self.cache[key] = value
            else:
                self.cache.popitem(last=False)
                self.cache[key] = value
        





# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

