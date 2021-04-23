def func1(n):
    sum1 = sum2 = 0
    for i in range(1, n + 1):
        sum1 += i
        sum2 += i ** 2
    res = sum1 ** 2 - sum2
    print(res)


def func2(n):
    # 等差数列公式和平方和公式
    sum1 = (1 + n) * n / 2
    sum2 = 1/6 * n * (n + 1) * (2 * n + 1)
    res = sum1 ** 2 - sum2
    print(res)


func1(100)
func2(100)
