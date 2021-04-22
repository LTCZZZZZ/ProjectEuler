upper = 4000000


def fibonacci(m):
    # 最大项不超过m的斐波那契数列
    l = [1, 2]
    while True:
        num = l[-2] + l[-1]
        if num <= m:
            l.append(num)
        else:
            break
    return l


l = fibonacci(upper)
print(l)
print(len(l))
# 较慢的方法1
res1 = sum([x if x % 2 == 0 else 0 for x in l])
# 较慢的方法2
res2 = sum(filter(lambda x: x % 2 ==0, l))
# 注意到数列的偶数项序数为2，5，8，11......
res3 = sum(l[1::3])
print(res1)
print(res2)
print(res3)
