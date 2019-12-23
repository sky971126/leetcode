"""
Description
Assuming we have an infinite coordinate system. Someone starts from (0, 0) and he can go up, left 
and right without passing one place. Ask how many paths he can have if he can walk n steps.

constraints
go up, left and right: he cannot go down.
without passing one place: e.g. cannot go left and go right consecutively.
"""

def find_paths(n):
    # candidate only need to return a interger number
  if n == 0:
    return 0
  dp = [0] * (n + 1)
  dp[0] = 1
  
  for i in range(1,n+1):
    dp[i] = 2 + dp[i-1]
    for j in range(1, i): # j steps to left or right 
      dp[i] += 2 * dp[i-j-1]
  return dp[n]


print(find_paths(0)) # 0
print(find_paths(1)) # 3
print(find_paths(2)) # 7
print(find_paths(3)) # 7