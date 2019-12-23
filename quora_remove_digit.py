import collections
ct = collections.Counter([1,2,2,2,3,4,4])
lt = list(ct.items())
lt.sort(key=lambda x: (x[1],x[1]))
print(lt)