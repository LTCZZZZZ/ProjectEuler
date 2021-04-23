import collections
import math
from problem3 import get_factors, prime_list


def func1():
    # 一般对分散的多个数求最小公倍数用此种方法较好，对连续的，建议使用func2
    statistics = collections.Counter()
    # &是Counter类型对每个key取最小的，|是Counter类型对每个key取最大的
    for i in range(2, 21):
        factors = get_factors(i)
        statistics |= collections.Counter(factors)
    print(statistics)
    res = 1
    for k, v in statistics.items():
        res *= k ** v
    print(res)


def func2(n):
    # 思想是取小于等于20的 每个素因子的不超过20的最大幂 作为乘数
    prime_nums = prime_list(n)  # [2, 3, 5, 7, 11, 13, 17, 19]
    # print(prime_nums)
    res = 1
    for p in prime_nums:
        for i in range(1, 6):
            if p ** i > n:
                res *= p ** (i - 1)
                break
    print(res)


def func3(n):
    # 比func2进一步优化的版本
    prime_nums = prime_list(n)  # [2, 3, 5, 7, 11, 13, 17, 19]
    # print(prime_nums)
    res = 1
    for p in prime_nums:
        i = math.floor(math.log(n, p))
        res *= p ** i
    print(res)


func1()
func2(20)
func3(20)
