def solution(k,n):
    res = []
    people = list(range(1,n+1))
    index = 0
    while len(res) < n-1:
        remain = len(people)
        index = (k + index - 1) % remain
        res.append(people[index])
        del(people[index])
    return res

print(solution(3,5))