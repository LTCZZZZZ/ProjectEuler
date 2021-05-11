import numpy as np
import itertools
from scipy.special import comb  # 排列组合函数
from functools import lru_cache
from tools import timer  # 注意此处需ProjectEuler目录加入PYTHONPATH，否则会报错
# 在pycharm运行时自动做了这一点，可用下面两行代码检验
# import sys
# print(sys.path)

@timer
@lru_cache(maxsize=128)
def compute1(m, n):
    if m == 0 or n == 0:
        return 1
    else:
        return compute1(m - 1, n) + compute1(m, n - 1)


@timer
def compute2(m, n):
    # O(mn) time and O(mn) memory
    matrix = np.ones([m + 1, n + 1], dtype=int)
    # print(matrix.dtype)  # int64，如果用int32会溢出
    for i, j in itertools.product(range(m), range(n)):
        # 从第二行第二列开始计算
        matrix[i + 1, j + 1] = matrix[i, j + 1] + matrix[i + 1, j]
    # print(matrix)
    return matrix[-1, -1]


# compute1如果不加@lru_cache超过120s仍得不到结果，加上后速度大幅提高，但也不如compute2
print(compute1(20, 20))
print(compute2(20, 20))

# 另解：这只是一个简单的组合问题，即从(m + n)步中任选出m步向右走共有多少种选法，
# 比compute2快超过100倍，O(n) time and O(1) memory
comb = timer(comb)
print(comb(40, 20, exact=True))
