#
# @lc app=leetcode id=975 lang=python3
#
# [975] Odd Even Jump
#
import math

class Solution:
    def oddEvenJumps(self, A):
        if len(A) == 1:
            return 1
        A_sort = list(enumerate(A))
        A_sort.sort(key=lambda x: x[1]+x[0]/20001)
        N = len(A)
        odd_next = [0] * N
        odd_next[-1] = N-1
        even_next = [0] * N
        even_next[-1] = N-1
        mono = []
        for i in range(N):
            index, value = A_sort[i]
            if mono: # and value >= mono[-1][1]:
                temp = []
                for j in range(len(mono)-1,-1,-1):
                    item = mono[j]
                    if item[0] < index:
                        odd_next[item[0]] = index
                    else:
                        temp.append(item)
                mono = list(reversed(temp))
            mono.insert(0, A_sort[i])

        A_sort.sort(key=lambda x: x[1]-x[0]/20001, reverse=True)
        mono = []
        for i in range(N):
            index, value = A_sort[i]
            if mono:# and value <= mono[-1][1]:
                temp = []
                for j in range(len(mono)-1,-1,-1):
                    item = mono[j]
                    if item[0] < index:
                        even_next[item[0]] = index
                    else:
                        temp.append(item)
                mono = list(reversed(temp))
            mono.append(A_sort[i])

        res = 0
        odd = True
        for i in range(N):
            odd = False
            nex = odd_next[i]
            while 1:
                if nex == 0:
                    break
                if nex == N-1:
                    res += 1
                    break
                if odd:
                    nex = odd_next[nex]
                else:
                    nex = even_next[nex]
                odd = not odd
        print(odd_next, even_next)
        return res
        

class Solution():
    def oddEvenJumps(self, A):
        N = len(A)

        def make(B):
            ans = [None] * N
            stack = []  # invariant: stack is decreasing
            for i in B:
                while stack and i > stack[-1]:
                    ans[stack.pop()] = i
                stack.append(i)
            return ans

        B = sorted(range(N), key = lambda i: A[i])
        print(B)
        oddnext = make(B)
        B.sort(key = lambda i: -A[i])
        evennext = make(B)

        odd = [False] * N
        even = [False] * N
        odd[N-1] = even[N-1] = True
        print(oddnext,evennext)
        for i in range(N-2, -1, -1):
            if oddnext[i] is not None:
                odd[i] = even[oddnext[i]]
            if evennext[i] is not None:
                even[i] = odd[evennext[i]]

        return sum(odd)

print(Solution().oddEvenJumps([1,0,3,3,4]))

    def binarySearch_l(self, A, target):
        l, r = 0, len(A)-1
        m = 0
        while (l<=r and l>-1 and r<len(A)):
            m = int((l+r)/2)
            if  A[m][1] == target:
                if m == 0 or A[m-1][1] < target:
                    return m
                else:
                    r = m-1
            elif A[m][1] < target:
                l = m+1
            else:
                r = m-1
        return m

    def binarySearch_r(self, A, target):
        l, r = 0, len(A)-1
        m = 0
        while (l<=r and l>-1 and r<len(A)):
            m = int((l+r)/2)
            if  A[m][1] == target:
                if m == len(A)-1 or A[m+1][1] > target:
                    return m
                else:
                    l = m+1
            elif A[m][1] < target:
                l = m+1
            else:
                r = m-1
        return m
"""
            
