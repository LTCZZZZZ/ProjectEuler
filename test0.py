from collections import Counter
from functools import reduce

a = Counter(range(1, 6))
a[1] -= 1
print(a)
print(sum(a))
print(a.items())

r = reduce(lambda x, y: x * y, [i + 1 for _, i in a.items()])
print(r)
