#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == "(":
                stack.append(0)
            elif i == ")":
                if stack == []:
                    return False
                if stack[-1]!=0:
                    return False
                else:
                    stack.pop(-1)
            elif i == "{":
                stack.append(1)
            elif i == "}":
                if stack == []:
                    return False
                if stack[-1]!=1:
                    return False
                else:
                    stack.pop(-1)
            elif i == "[":
                stack.append(2)
            elif i == "]":
                if stack == []:
                    return False
                if stack[-1]!=2:
                    return False
                else:
                    stack.pop(-1)
        if stack == []:
            return True
        else:
            return False

