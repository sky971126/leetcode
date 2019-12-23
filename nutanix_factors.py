
n = 110

for i in range(2,n+1):
    if n % i == 0:
        while n % i == 0:
            n = n / i
            print(i)
    if n == 1:
        break