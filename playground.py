a = [[1,10,4],[1,10,6],[2,10,2],[1,11,5]]
a.sort(key=lambda x: (x[0],x[1],x[2]))
print(a)