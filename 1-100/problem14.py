# Collatz Problem（考拉兹序列问题）
# 反过来想，只要证明从1开始，按规则能覆盖所有的自然数即可。另一种思维如下：
# 假设存在一个N不收敛到1，那么有两种情况，一种是数列趋于无穷大，一种是形成一个闭环
# 先证明这样的闭环不存在：假设存在这样的闭环，这此环中至少存在一个大奇数N
import time


def collatz(n):
    m = n  # 先将初始的数存起来，最后发现好像不需要
    chain = []
    while n > 1:
        # print(n)

        # 将前面的结果存起来，避免重复调用（但其实会有内存方面的问题）
        if n in d:
            # 此时chain中的元素都是d中没有的，故而全部添加进去
            length = len(chain)
            for i, v in enumerate(chain):
                d[int(v)] = length - i + d[n]
            # 如果是这种情况下，直接返回m，其他情况返回None，此时也不需要break了
            return m
            # break
        else:
            chain.append(n)

        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
    return None


time1 = time.time()
d = {2: 1}  # 根据collatz函数的逻辑，需要初始值，且不能为{1:0}，


# d[27]=111

# 当循环不断执行时，显然，最后添加进d的元素必然链最长，故此将其存起来避免了最后一百万个数取max的操作
# 注意，上一行的注释是错误的，因为树是分叉的，最后添加进d的元素只能说是树的当前末端，而并非全局最长
# num = 0
# for i in range(0, 10 ** 3):
#     res = collatz(i)
#     if res:
#         num = res
# print(d)
# print(max(d.values()), num, d[num])


# 约1.84s，如果从0开始约2.1s
# for i in range(500000, 10 ** 6):
#     collatz(i)
# # print(max(d.values()))
# len_c = 1
# num = 0
# # print(d) # 如果加上打印，因为d长度超过100w，时间直接增加0.5s
# for k, v in d.items():
#     if v > len_c:
#         len_c = v
#         num = k
# print(num, len_c)
# time2 = time.time()
# print(time2 - time1)


# 官方解法，逻辑基本相同，但确实看起来简洁明晰了许多，这里values里面每个值比d里面大1，表示链中的元素个数
# 经测试大约只需要1s，比我之前的方法快了不少
# values = {1: 1}
# def countChain(n):
#     if n in values:
#         return values[n]
#
#     if n % 2 == 0:
#         values[n] = 1 + countChain(n / 2)
#     else:
#         values[n] = 2 + countChain((3 * n + 1) / 2)
#
#     return values[n]
#
#
# len_c = 1
# num = 0
# for i in range(500000, 10 ** 6):
#     if (temp := countChain(i)) > len_c:
#         len_c = temp
#         num = i
# print(num, len_c)
# time2 = time.time()
# print(time2 - time1)


# 此方法大约只需0.8s，
# 大小是最后才比较的，
# 并且跑了从2到100w的所有数，
# 而且，是从2逐一增大的，很多结果没有复用，竟然比官方更快！就离谱！！
# 猜想：官方方法有一个递归深度开辟执行空间内存的问题，它这儿没有，
# 另外，当values很大的时候，判断n in values也需要一定的开销，此处也没有（此处是用x<i这个简单的判断，但付出的代价是有很多结果没有储存起来复用）
def main(N=10 ** 6):
    d = {}
    for x in range(2, N):
        i, n = x, 0
        while x != 1:
            if x < i:
                n = n + d[x]
                break
            elif x % 2 == 0:
                x = x // 2
                n += 1
            else:
                x = (3 * x + 1) // 2
                n += 2
        d[i] = n
    return max(d, key=d.get)  # 注意这种比大小的写法


print(main())
time2 = time.time()
print(time2 - time1)
