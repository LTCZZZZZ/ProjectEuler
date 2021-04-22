# 参见 https://blog.csdn.net/SL_World/article/details/86507872


def d():
    print('初始化')
    sum = 0
    value = yield sum
    sum = sum + value
    print('sum的值是：%d' % sum)
    value = yield sum
    sum = sum + value
    print('sum的值是：%d' % sum)
    value = yield sum
    sum = sum + value
    print('sum的值是：%d' % sum)
    return sum + 1


c = d()  # c是一个生成器，此行代码并不运行d()内容
a = c.send(None)  # 启动生成器，遇到d()的第一个yield时中断
print('生成器传出的值:%d' % a)
a = c.send(1)
print('生成器传出的值:%d' % a)
a = c.send(8)
print('生成器传出的值:%d' % a)

try:
    a = c.send(20)
except StopIteration as e:
    print('生成器传出最后的值:%d' % e.value)

# 当运行a = c.send(None)时，启动生成器函数，在第一个yield中断，此时这行程序仅仅运行了yield sum并没有开始赋值，
# 而yield sum就相当于return sum，即向函数外传出sum，所以函数外接收值的变量a存储的值是0。
# 当运行a = c.send(1)时，我们继续启动生成器函数开始运行value = yield，并向生成器函数的第一个中断点yield传递
# 了值1，然后通过yield把1传递给了value并通过后续计算累加sum。程序直到第二个yield中断，向函数外返回第二个sum。
# 以此类推。

# 【注】：
# 1）第一个send(None)填入的参数必须是None，因为在启动生成器函数到第一次中断，程序只运行到第一个yield sum，
# 没有赋值语句，所以只能填None。
# 2）对于生成器函数最后的return sum语句并不向函数外传递sum，而是会在迭代结束时报错StopIteration: 3，
# 返回值sum包含在StopIteration的value中，也就是3，可以捕获StopIteration在函数外得到这个值。
# 把上面代码中的a = c.send(None)之后的代码改成如下代码即可。

