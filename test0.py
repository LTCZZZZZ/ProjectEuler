from collections import Counter
from functools import reduce
import numpy as np
import itertools
from scipy.special import comb, perm  # 排列组合函数
from functools import lru_cache  # 缓存机制


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

print(np.ones([3, 2]))
print(list(itertools.product(range(3), repeat=2)))
print(list(itertools.product('ABC', 'abc', '123')))
print(comb(6, 3), perm(6, 3, exact=True))

t = np.pad([6, 7], [1, 2], 'constant', constant_values=[0, 0])
print(t)

print(np.prod(range(1, 9)))  # 连乘
print(sum([]))

