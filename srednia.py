import numpy as np

a=[1, 0, 4, 3]

avg = sum(a) / len(a)
var = sum((x-avg)**2 for x in a) / len(a)
print(var)

print(np.var([1, 0, 4, 3]))