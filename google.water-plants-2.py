def water_plant(plants, c1, c2):
    if not plants:
        return 0
    l = 0
    r = len(plants) - 1
    w1 = 0
    w2 = 0
    res = 0
    while (l < r):
        if w1 < plants[l]:   
            w1 = c1
            res += 1
        w1 -= plants[l]
        l += 1
        
        if w2 < plants[r]:
            w2 = c2
            res += 1
        w2 -= plants[r]
        r -= 1
    
    if l == r and (w1 + w2) < plants[l]:
        res += 1
    
    return res

print(water_plant([2, 4, 5, 1, 2], 5, 7))