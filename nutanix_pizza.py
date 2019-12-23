def solution(A):
    carry = 0
    for i in A:
        if i - carry < 0:
            return False
        carry = (i - carry) % 2
    if carry > 0:
        return False
    else:
        return True
print(solution([1,2,1,2])) # True
print(solution([5,4,3,7,7])) # True
print(solution([1,2,2,2])) # False
print(solution([1,0])) # False
print(solution([])) # True
