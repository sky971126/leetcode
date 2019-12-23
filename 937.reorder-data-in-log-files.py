#
# @lc app=leetcode id=937 lang=python3
#
# [937] Reorder Data in Log Files
#

# @lc code=start
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        log_alpha = []
        log_digit = []
        for log in logs:
            log_split = log.split()            
            if 48 <= ord(log_split[1][0]) <= 57:
                log_digit.append(log)
            else:
                log_alpha.append([log_split[0], " ".join(log_split[1:])])
        log_alpha.sort(key=lambda x: (x[1], x[0]))
        return [" ".join(log) for log in log_alpha] + log_digit

# @lc code=end

