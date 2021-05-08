from collections import Counter
from functools import reduce

a = Counter(range(1, 6))
a[1] -= 1
print(a)
print(sum(a))
print(a.items())

r = reduce(lambda x, y: x * y, [i + 1 for _, i in a.items()])
print(r)

print(5 == 5.0)
# print(5 is 5)
# print(5 is 5.0)
d = {5: 2, 30: 1, 6: 6}
print(d[5])
print(d[5.0])
print(d.get)
print(max(d, key=d.get))
