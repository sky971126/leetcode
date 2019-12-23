class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n:
            if n % 2 == 1:
                res += 1
            n = n >> 1
        return res