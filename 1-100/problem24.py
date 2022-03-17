import math

print(math.factorial(10))

l = list(range(10))  # 1到10数字
n = 10 ** 6 - 1 # 位次，想想这里为什么要减1？？我这里没考虑边界条件一开始出错了
s = []  # 待排列填充的列表

divisors = []
d = 1
for i in range(1, 10):
    d *= i
    divisors.append(d)
divisors.reverse()
print(divisors)

for div in divisors:
    print(n // div)  # 想想这个结果为什么不可能大于len(l) - 1？这很自然但也很重要，它保证下面的l.pop()操作不会报错
    print(l)
    s.append(l.pop(n // div))  # 这一行代码信息量很大
    n = n % div
s.append(l[0])

s = ''.join(map(str, s))
print(s)
