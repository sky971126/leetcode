#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start
import math
import queue
class Solution:
    """DFS TLE
    def numSquares(self, n: int) -> int:
        dp = [None] * (n+1)
        dp[0] = 0
        dp[1] = 1

        def numSquares_helper(n):
            if n < 0:
                return None
            if dp[n] != None:
                return dp[n]
            min_num = n
            for i in range(1, int(math.sqrt(n))+1):
                num = numSquares_helper(n - i*i)
                if num != None:
                    min_num = min(min_num, num+1)
            dp[n] = min_num
            return min_num
        return numSquares_helper(n)
    """
    # use set instead of queue to avoid duplicate
    def numSquares(self, n: int) -> int:
        que = set()
        que.add(n)
        min_num = 1
        while que:
            new_que = set()
            for num in que:
                for i in range(1, int(math.sqrt(num))+1):
                    new = num - i * i
                    if new == 0:
                        return min_num
                    new_que.add(new)
            que = new_que
            min_num += 1
        return None
    """
    def numSquares(self, n):

        # list of square numbers that are less than `n`
        square_nums = [i * i for i in range(1, int(n**0.5)+1)]
    
        level = 0
        queue = {n}
        while queue:
            level += 1
            #! Important: use set() instead of list() to eliminate the redundancy,
            # which would even provide a 5-times speedup, 200ms vs. 1000ms.
            next_queue = set()
            # construct the queue for the next level
            for remainder in queue:
                for square_num in square_nums:    
                    if remainder == square_num:
                        return level  # find the node!
                    elif remainder < square_num:
                        break
                    else:
                        next_queue.add(remainder - square_num)
            queue = next_queue
        return level
    """


# @lc code=end

print(Solution().numSquares(104))