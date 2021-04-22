
def func1():
    # 逻辑简单但运行时间长的版本
    sum = 0
    for i in range(3, 1000, 3):
        sum += i
    for i in range(5, 1000, 5):
        if i % 3 == 0:
            continue
        sum += i
    print(sum)


def func2():
    # 利用等差数列，逻辑稍复杂但运算少很多

    def sum(a, b, d):
        # a为首项，b为末项，d为公差，求等差数列的和
        return (a + b) * ((b - a) / d + 1) / 2

    res = sum(3, 999, 3) + sum(5, 995, 5) - sum(15, 990, 15)
    print(res)


func1()
func2()
