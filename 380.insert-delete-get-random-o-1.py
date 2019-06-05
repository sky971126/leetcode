#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#
class RandomizedSet:
    import random 

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num_dict = {}
        self.num_list = []
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.num_dict:
            return False
        else:
            self.num_dict[val] = len(self.num_list)
            self.num_list.append(val)
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.num_dict:
            return False
        else:
            index = self.num_dict[val]
            if index == len(self.num_list) - 1:
                del self.num_list[-1]
                del self.num_dict[val]
            else:
                self.num_list[index] = self.num_list[-1]
                del self.num_list[-1]
                del self.num_dict[val]
                self.num_dict[self.num_list[index]] = index
            return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        if self.num_list:
            ran = random.randint(0, len(self.num_list) - 1)
            return self.num_list[ran]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

