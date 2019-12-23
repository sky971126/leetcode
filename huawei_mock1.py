import math
#_, p, pm, d, dm = [int(i) for i in input().split("|")]
#print(p, pm, d, dm)

def phone(p, pm):
    p = math.ceil(p/60)
    money = 0
    if p <= 1:
        return 0
    p -= 1
    if p <= 4:
        money += p * pm * 1.5
        return int(money / 10)
    money += 4 * pm * 1.5
    p -= 4
    if p <= 5:
        money += p * pm
        return int(money / 10)
    money += 5 * pm
    p -= 5
    if p <= 10:
        money += p * pm * 0.5
        return int(money / 10)
    money += 10 * pm * 0.5
    p -= 10
    money += p * pm * 0.2
    return int(money / 10)
print(phone(1801,200))

def MB(KB):
    return KB * 1024

def digit(d, dm):
    if d <= MB(100): # 100
        return d
    if d <= MB(125): # gift
        return MB(100)
    d -= MB(25)

    if d <= MB(200): # 200
        return d
    if d <= MB(300): # gift
        return MB(200)
    d -= MB(100)

    if d <= MB(500): # 500
        return d
    d -= MB(500)
    count = MB(500)
    while (1):
        if d < MB(100):
            count += d
            return count
        elif d < MB(200):
            count += MB(100)    
            return count
        else:
            d -= MB(200)
            count += MB(100)    

print(int(digit(807936,3)*0.03))