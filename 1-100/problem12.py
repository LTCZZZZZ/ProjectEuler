import math
from collections import Counter
from functools import reduce


def get_factors(n, l=[2, 3]):
    # 为了避免重复计算素数列表l，对problem3中的函数有所改进

    # 这是一个素因子分解函数，
    # 思想是，从两边出发，首先依次取l中的元素a看是否为m的因子，
    # 类似于素因子分解的思想，如果a是，命m=m/a，再测试a是否为m的因子，直到不是为止，
    # 此时进入下一个循环，测试b；并且，只有当l中的元素被耗尽时，才更新l
    # 放到程序中就是，l中每加入一个新数，就将此数作为因子对m进行测试

    # l = [2, 3]

    def get_prime():
        # 这里用素数生成器模型，详细的生成器模型参见generator_test.py
        k = 0
        while True:
            try:
                a = l[k]
                now_n = yield a
                k += 1
            except IndexError:
                # 大于3的素数必为奇数，从l的最后一个元素开始向上每次加2
                #
                p = l[-1] + 2
                # print(p, now_n)
                while p <= round(math.sqrt(now_n)):  # 因为此时now_n中已经不含小于等于l[-1]的因子了，故可以这样写
                    for j in l:
                        # print(p, j)
                        if j > round(math.sqrt(p)):  # 为防可能的程序计算精度误差，这里用一下round
                            l.append(p)
                            now_n = yield p
                            # print(p, now_n)
                            break
                        if p % j == 0:
                            break
                    p += 2
                # 这里若执行完全部循环还没yield，则表示剩余的因子就是素数
                # 也可能上面的while循环在某次yield获得新的now_n后不满足条件，一次都没有执行，此时也能得出now_n是素数或1
                return now_n

    factors = []
    sqrt_n = round(math.sqrt(n))
    prime_generator = get_prime()
    a = prime_generator.send(None)
    while a <= sqrt_n:
        while n % a == 0:
            n = int(n / a)
            factors.append(a)
        else:
            try:
                a = prime_generator.send(n)
                sqrt_n = round(math.sqrt(n))
            except StopIteration as e:  # 此时n即为素因子或1
                if e.value != 1:
                    factors.append(e.value)
                break
    else:
        # 只有在n<=6或n为2的某次幂时会执行到此处，n>=7时都由StopIteration后退出循环
        if n != 1:
            factors.append(n)

    print(l)
    print(factors)
    return l, factors


def compute_divisors0(factors):
    # 根据素因子列表计算m的因数个数
    # 常规的简单代码计算方式，但运行应该比下面的compute_divisors慢
    return reduce(lambda x, y: x * y, [i + 1 for _, i in Counter(factors).items()])


def compute_divisors(factors):
    # 根据素因子列表计算m的因数个数
    # 因为factors是按序排列的，所以计数相乘时比一般的无序列表要简单
    res = 1
    f = factors[0]
    k = 1  # k记录相同因子个数的增加
    i = 1
    while True:
        k += 1
        try:
            print(f, factors[i], k)
            if f != factors[i]:
                res *= k
                f = factors[i]
                k = 1
            i += 1
        except IndexError:
            res *= k
            break
    print(f'divisors: {res}')
    return res


def func1():
    i = 2
    l = [2, 3]
    while True:
        m = i * (i + 1) / 2
        l, factors = get_factors(m, l)  # 这里每次循环利用l，即每次不用重头计算素数列表
        # if compute_divisors0(factors) > 500:
        if compute_divisors(factors) > 500:
            print(i, m)
            break
        i += 1


# 事实上，还可以进一步加速

# 一种方法是（注意下面两种方法都基于n和(n+1)互质，即没有大于1的公因子）
# D(t) = D(n/2) * D(n+1) if n is even
# or D(t) = D(n) * D((n+1)/2)) if (n+1) is even

# 另一种方法是计算出n和(n+1)的素因子列表的并集(此并集非集合意义上的并集)再移除一个2，然后针对此factors计算
def func2():
    i = 2
    l = [2, 3]
    while True:
        l, factors1 = get_factors(i, l)  # 这里每次循环利用l，即每次不用重头计算素数列表
        l, factors2 = get_factors(i + 1, l)
        counter = Counter(factors1) + Counter(factors2)
        counter[2] -= 1
        if reduce(lambda x, y: x * y, [i + 1 for _, i in counter.items()]) > 500:
            print(i, i * (i + 1) / 2)
            break
        i += 1


# func1()
func2()  # 运行显示func2比func1快了N倍不止
