import collections

def solution(s, t):
    D = collections.OrderedDict()
    for i in range(len(s)):
        if s[i] in D:
            D[s[i]].append(i)
        else:
            D[s[i]] = [i]
    T = collections.OrderedDict()
    for i in range(len(t)):
        if t[i] in T:
            T[t[i]].append(i)
        else:
            T[t[i]] = [i]

    while D and T:
        print(D, T)
        if D.popitem()[1] != T.popitem()[1]:
            return False
    print(D, T)
    if D or T:
        return False
    return True
print(solution("aabc","ddep"))