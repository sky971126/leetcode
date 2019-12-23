#
# @lc app=leetcode id=301 lang=python3
#
# [301] Remove Invalid Parentheses
#

# @lc code=start
class Solution:
    def removeInvalidParentheses(self, s: str):
        left = 0 #excessive left
        right = 0 #excessive right
        for i in s:
            if i == "(":
                left += 1
            elif i == ")":
                left -= 1
                if left < 0:
                    right += 1
                    left = 0
        res_set = set()
        def removeInvalidParentheses_helper(index, l, r, left_count, right_count, res):
            if l > left or r > right or left_count < right_count:
                return
            if index == len(s):
                if left_count == right_count:
                    res_set.add(res)
                return
            if s[index] == "(":
                #remove
                removeInvalidParentheses_helper(index+1, l+1, r, left_count, right_count, res)
                #not remove
                removeInvalidParentheses_helper(index+1, l, r, left_count+1, right_count, res+"(")
            elif s[index] == ")":
                #remove
                removeInvalidParentheses_helper(index+1, l, r+1, left_count, right_count, res)
                #not remove
                removeInvalidParentheses_helper(index+1, l, r, left_count, right_count+1, res+")")
            else:
                removeInvalidParentheses_helper(index+1, l, r, left_count, right_count, res+s[index])
        removeInvalidParentheses_helper(0, 0, 0, 0, 0, "")
        return list(res_set)
# @lc code=end
#Solution().removeInvalidParentheses(")((()))((")
