def water_plant(plants, capacity):
    if not plants:
        return 0
    res = 0
    water = capacity
    for i in range(len(plants)):
        step = i #step needed to refill
        if plants[i] < water:
            res += 1
            water -= plants[i]
        else:
            res += 2 * step + 1
            water = capacity - plants[i]
    return res

print(water_plant([2,4,5,1,2], 6))
