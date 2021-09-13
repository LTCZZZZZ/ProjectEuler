from problem12 import get_factors
from collections import Counter
from itertools import product
import numpy as np


amicable_nums = []
l = [2, 3]
# print(get_factors(1))

def sum_divisors(factors):
    # 由素因子列表得出因子列表，包括1，再计算其和
    sub_factors = []
    for k, v in Counter(factors).items():
        # 比如k = 2, v = 3，就生成[1, 2, 4, 8]
        sub_factors.append([k ** i for i in range(v + 1)])  # 0的0次方居然不报错，会被记为1
    # 对sub_factors计算笛卡尔积，将得到的结果(列表的列表)中最内层列表求连乘积，即得到divisors列表，
    # 去掉外层列表最后一个元素，求和，即得结果
    return sum([np.prod(i) for i in product(*sub_factors)][:-1])  # 不计算最后一个元素（自己本身）


for n in range(2, 10000):
    if n in amicable_nums:
        continue
    l, factors = get_factors(n, l)
    # print('f1', factors)
    m = sum_divisors(factors)  # 8128自己和自己相等
    if m != n:
        l, factors = get_factors(m, l)
        # print('f2', factors)
        if sum_divisors(factors) == n:
            amicable_nums.extend([m, n])
            print(m, n)


# print(sum_divisors([0]))  # 会等于1
print(amicable_nums)
print(sum(amicable_nums))
