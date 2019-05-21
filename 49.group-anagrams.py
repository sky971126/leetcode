#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs:
            count = 26 * [0]
            for c in s:
                count[ord(c)-97] += 1
            count_tuple = tuple(count)
            if count_tuple in dic:
                dic[count_tuple].append(s)
            else:
                dic[count_tuple] = [s]
        return list(dic.values())

#print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
