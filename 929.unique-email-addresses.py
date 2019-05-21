#
# @lc app=leetcode id=929 lang=python3
#
# [929] Unique Email Addresses
#
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        UNIQUE = set()
        result = 0
        for email in emails:
            local, domain = email.split("@")
            local = local.split("+")[0]
            local = local.replace(".","")
            UNIQUE.add(local+'@'+domain) 
        return len(UNIQUE)

