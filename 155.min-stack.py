#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.stack_min = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.stack_min or x < self.stack_min[-1]:
            self.stack_min.append(x)
        else:
            self.stack_min.append(self.stack_min[-1])

    def pop(self) -> None:
        pop_item = self.stack[-1]
        del self.stack[-1]
        del self.stack_min[-1]
        return pop_item

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack_min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

