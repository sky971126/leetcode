def solution(s):
    res = ""
    for i in range(0,len(s)//2):
        res += s[2*i+1] + s[2*i]
    if len(s) % 2 == 1:
        res += s[-1]
    return res

print(solution("abcdefg"))