import math
def maxArithmeticLength(a,b):
    g = 0
    set_ab = set(a) | set(b)
    if len(a) > 1:
        g = a[1] - a[0]
        for i in range(1, len(a)-1):
            g = math.gcd(a[i+1] - a[i], g)
    else:
        res_max = 0
        for i in range(len(b)):
            bi = b.pop(0)
            res_max = max(res_max, maxArithmeticLength(sorted([a[0],bi]),b))

        return res_max
    res_max = 0
    for i in range(1, g+1):
        if g % i == 0:
            res = 0
            for j in range(a[0], a[-1]+i, i):
                if j in set_ab:
                    res += 1
                else:
                    res = 0
                    break
            if res:
                cur = a[0]
                while cur - i in set_ab:
                    res += 1
                    cur = cur - i
                cur = a[-1]
                while cur + i in set_ab:
                    res += 1
                    cur = cur + i
                res_max = max(res_max, res)
    if res_max:
        return res_max
    return -1

print(maxArithmeticLength([11], [5,9,12,16,22]))