import math


def prime_list(n):
    # 最大不超过n的素数列表
    l = [2, 3]
    for i in range(5, n + 1, 2):  # 大于3的素数必为奇数
        for j in l:
            if j > round(math.sqrt(i)):  # 为防可能的程序计算精度误差，这里用一下round
                l.append(i)
                break
            if i % j == 0:
                break
        # 由伯特兰—切比雪夫定理易知p和p^2之间至少存在一个素数，故此else子句无必要，因为for循环中必然触发break
        # 伯特兰—切比雪夫定理说明：若整数n > 3，则至少存在一个质数p，符合n < p < 2n − 2
        # else:
        #     l.append(i)
    return l


def func1():
    # 比较笨拙的解法，耗时较长
    for i in reversed(prime_list(round(math.sqrt(m)))):
        if m % i == 0:
            print(i)
            break
    else:
        print(f'{m}是质数')


def get_factors(n):
    # 这是一个素因子分解函数，
    # 思想是，从两边出发，首先依次取l中的元素a看是否为m的因子，
    # 类似于素因子分解的思想，如果a是，命m=m/a，再测试a是否为m的因子，直到不是为止，
    # 此时进入下一个循环，测试b；并且，只有当l中的元素被耗尽时，才更新l
    # 放到程序中就是，l中每加入一个新数，就将此数作为因子对m进行测试
    l = [2, 3]

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
    return factors


if __name__ == '__main__':
    m = 600851475143
    # func1()
    get_factors(m)  # 测试表明func2比func1快很多倍
