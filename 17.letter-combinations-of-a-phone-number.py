#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
class Solution:
    def letterCombinations(self, digits):
        """
        num_dict = {}
        for i in range(2,7):
            ans = 3 * i + 91
            num_dict[i] = (chr(ans), chr(ans+1), chr(ans+2))
        num_dict[7] = ('p','q','r','s')
        num_dict[8] = ('t', 'u', 'v')
        num_dict[9] = ('w','x','y','z')
        print(num_dict)    
        """
        if digits == "":
            return []
        num_dict = {2: ('a', 'b', 'c'), 3: ('d', 'e', 'f'), 4: ('g', 'h', 'i'), 5: ('j', 'k', 'l'), 6: ('m', 'n', 'o'), 7: ('p', 'q', 'r', 's'), 8: ('t', 'u', 'v'), 9: ('w', 'x', 'y', 'z')}
        results = []
        self.letterCombinations_helper(digits, 0, num_dict, '', results)
        return results
    
    def letterCombinations_helper(self, digits, i, num_dict, result, results):
        if i >= len(digits):
            results.append(result)
        else:
            num = int(digits[i])
            for j in num_dict[num]:x
                self.letterCombinations_helper(digits, i+1, num_dict, result + j, results)

#Solution().letterCombinations("23")