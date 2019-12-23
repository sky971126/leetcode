n = int(input())
s = set()
for i in range(n):
    num = int(input())
    s.add(num)
for i in sorted(list(s)):
    print(i)