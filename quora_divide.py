def solution(A):
    less = set()
    more = set()
    for i in A:
        if len(more) < len(less):
            less, more = more, less
        if i in less and i in more:
            return []
        elif i in less:
            more.add(i)
        else:
            less.add(i)
    return [less,more]

print(solution([1,2,1,3,4,3,5,10,1,1]))