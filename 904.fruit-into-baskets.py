#
# @lc app=leetcode id=904 lang=python3
#
# [904] Fruit Into Baskets
#
class Solution:
    def totalFruit(self, tree):
        n = len(tree)
        if n <= 1:
            return n
        max_fruit = 0
        cur_fruit = 0
        near_type = 0
        far_type = 0
        tree_types = {}
        for i in range(n):
            if tree[i] in tree_types or len(tree_types) < 2:
                cur_fruit += 1
                tree_types[tree[i]] = i
                for j in tree_types:
                    if j != tree[i]:
                        far_type = j
                near_type = tree[i]
            else:
                index = tree_types[far_type]
                tree_types.pop(far_type)
                max_fruit = max(max_fruit, cur_fruit)
                cur_fruit = i - index
                tree_types[tree[i]] = i
                for j in tree_types:
                    if j != tree[i]:
                        far_type = j
                near_type = tree[i]
        max_fruit = max(max_fruit, cur_fruit)
        return max_fruit

#print(Solution().totalFruit([1,1,6,5,6,6,1,1,1,1]))

