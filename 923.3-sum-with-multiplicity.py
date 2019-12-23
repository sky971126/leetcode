#
# @lc app=leetcode id=923 lang=python3
#
# [923] 3Sum With Multiplicity
#

# @lc code=start
import collections
class Solution:
    # separate count
    """
    def threeSumMulti(self, A: List[int], target: int) -> int:
        ct = collections.defaultdict(int)
        if len(A) < 3:
            return 0
        ct[A[0]] += 1
        ct[A[1]] += 1
        res = 0
        for i in range(2,len(A)):
            target_i = target - A[i]
            ht = set() # unnecessary
            for key in ct.keys():
                if target_i - key in ht:
                    res += ct[key] * ct[target_i-key]
                elif target_i - key == key:
                    res += int(ct[key] * (ct[key]-1) / 2)
                else:
                    ht.add(key)
            ct[A[i]] += 1
        return res % (10**9+7)
    """
    # all count
    def threeSumMulti(self, A: List[int], target: int) -> int:
        ct = collections.Counter(A)
        keys = sorted(ct.keys())
        res = 0
        for i in range(len(keys)):
            key = keys[i]
            # use 3 times
            if target == 3 * key:
                #print(key,key,key, ct[key] * (ct[key]-1) * (ct[key]-2) / 6)
                res += ct[key] * (ct[key]-1) * (ct[key]-2) / 6
            # use 2 times
            target_i = target - 2 * key
            if target_i != key:
                #print(key,key,target_i, ct[key] * (ct[key]-1) * ct[target_i] / 2)
                res += ct[key] * (ct[key]-1) * ct[target_i] / 2
            # use 1 time
            target_i = target - key
            for j in range(i+1, len(keys)):
                if keys[j] == key or target_i - keys[j] == key:
                    continue
                if target_i - keys[j] in ct:
                    if target_i - keys[j] == keys[j]:
                        #print(key,keys[j],keys[j], ct[key] * ct[keys[j]] * ct[keys[j]] / 2)
                        res += ct[key] * ct[keys[j]] * (ct[keys[j]]-1) / 2
                    elif target_i - keys[j] < keys[j]:
                        #print(key,keys[j],target_i-keys[j],ct[key] * ct[keys[j]] * ct[target_i - keys[j]])
                        res += ct[key] * ct[keys[j]] * ct[target_i - keys[j]]
            ct.pop(key)
        return int(res) % (10**9+7)

        

# @lc code=end

