#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        self.generateParenthesis_helper(n, 0, 0, "", results)
        return results

    def generateParenthesis_helper(self, n, num_l, extra_l, par, results):
        if len(par) == 2*n:
            results.append(par)
            return
        if extra_l > 0:
            if num_l == n:
                while len(par) < 2*n:
                    par = par + ")"
                results.append(par)
                return
            else:
                self.generateParenthesis_helper(n, num_l+1, extra_l+1, par+"(", results)
                self.generateParenthesis_helper(n, num_l, extra_l-1, par+")", results)
        else:
            self.generateParenthesis_helper(n, num_l+1, extra_l+1, par+"(", results)

