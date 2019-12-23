#
# @lc app=leetcode id=1007 lang=python3
#
# [1007] Minimum Domino Rotations For Equal Row
#
"""
class Solution:
    def minDominoRotations(self, A, B):
        if not A or not B or len(A) != len(B):
            return -1
        a0 = A[0]
        b0 = B[0]
        rotate_a = self.rotation(a0, A, B)
        if rotate_a < 0:
            return self.rotation(b0, A, B)
        return rotate_a
            
    def rotation(self, x0, A, B):
        rotate_a = 0
        rotate_b = 0
        for i in range(len(A)):
            if A[i] != x0:
                if B[i] == x0:
                    rotate_a += 1
                else:
                    return -1
            if B[i] != x0:
                if A[i] == x0:
                    rotate_b += 1
        
        return min(rotate_a, rotate_b)
"""

class Solution:
    def minDominoRotations(self, A, B):
        if not A or not B or len(A) != len(B):
            return -1

        def find_min(target):
            A_min = 0
            B_min = 0
            for i in range(len(A)):
                if A[i] != target:
                    if B[i] == target:
                        A_min += 1
                    else:
                        return -1
                if B[i] != target:
                    if A[i] == target:
                        B_min += 1
            return min(A_min, B_min)
        
        res = find_min(A[0])
        if res < 0:
            res = find_min(B[0])
        return res


        

#print(Solution().minDominoRotations([1,2,1,1,1,2,2,2], [2,1,2,2,2,2,2,2]))
#print(Solution().minDominoRotations([1,2,1,1,1,2,2,2], [2,1,2,2,2,2,2,2]))
