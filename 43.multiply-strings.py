#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#
import math
class Solution:
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"
        if len(num1) > len(num2):
            num1, num2 = num2, num1
        products = []
        res = [0] * (len(num1) + len(num2))
        for _ in range(9):
            products.append([0] * (len(num1) + 1))
        for i in range(len(num2) - 1, -1, -1):
            digit = int(num2[i])
            if digit == 0:
                continue
            if products[digit-1][0] or (len(products[digit-1])>1 and products[digit-1][1]):
                self.add(res, products[digit-1], len(num2)-i-1)
            else:
                addon = 0
                for j in range(len(num1) - 1, -1, -1):
                    pro = int(num1[j]) * digit + addon
                    addon = 0
                    if pro > 9:
                        addon = int(math.floor(pro / 10))
                        pro = pro % 10
                    products[digit-1][j+1] = pro
                if addon:
                    products[digit-1][0] = addon
                self.add(res, products[digit-1], len(num2)-i-1)
        return "".join(str(i) for i in res)

    def add(self, res, num, offset):
        addon = 0
        for i in range(len(num)):
            res[len(num) - i - offset] += int(num[len(num) - 1 - i]) + addon
            if res[len(num) - i - offset] > 10:
                addon = 1
                res[len(num) - i - offset] -= 10
            else:
                addon = 0
        if addon:
            res[0] += 1
    
print(Solution().multiply("210","71"))

        

