import collections
import queue
def solution(A):
    hashmap = collections.defaultdict(list)
    hashmap[0] = [-1]
    diff_1_0 = 0
    res = 0
    for i in range(len(A)):
        if A[i]:
            diff_1_0 += 1
        else:
            diff_1_0 -= 1
        hashmap[diff_1_0].append(i)
        if len(hashmap[diff_1_0]) > 2:
            res = max(res, hashmap[diff_1_0][-1] - hashmap[diff_1_0][0])
    print(hashmap)
    return res




import collections
def solution2(A):
    D = {}
    res = 0
    D[0] = -1
    num_1_0 = 0
    for i in range(len(A)):
        num = A[i]
        if num == 1:
            num_1_0 += 1
        else:
            num_1_0 -= 1
        if num_1_0 in D:
            res = max(res, i - D[num_1_0])
        else:
            D[num_1_0] = i
    return res


print(solution([0,1,0,0,1,0,1,1,1,1,0,1]))
print(solution2([0,1,0,0,1,0,1,1,1,1,0,1]))










