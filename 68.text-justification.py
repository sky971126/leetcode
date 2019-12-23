#
# @lc app=leetcode id=68 lang=python3
#
# [68] Text Justification
#

# @lc code=start
class Solution:
    def fullJustify(self, words, maxWidth):
        doc = []
        line = []
        word_count = 0
        total_count = 0
        i = 0
        while(i < len(words)):
            word = words[i]
            if (line and total_count + len(word) + 1 > maxWidth):
                if len(line) == 1:
                    doc.append(line[0] + " " * (maxWidth-len(line[0])))
                else:
                    quotient = (maxWidth - word_count) // (len(line)-1)
                    remainder = (maxWidth - word_count) % (len(line)-1)
                    line_content = ""
                    for w in line[:-1]:
                        line_content += w + " " * quotient
                        if remainder:
                            line_content += " "
                            remainder -= 1
                    line_content += line[-1]
                    doc.append(line_content)
                line = [] # refresh line
                total_count = 0
                word_count = 0
                # i not change
            else:
                if line:
                    total_count += len(word) + 1
                else:
                    total_count += len(word) # beginning word
                word_count += len(word)
                line.append(word)
                i += 1
        if line:
            line_content = " ".join(line)
            doc.append(line_content + " " * (maxWidth-len(line_content)))
        return doc            

# @lc code=end

print(Solution().fullJustify(["Listen","to","many,","speak","to","a","few."],6))