import math

# 另外的解法：对第n个素数p有ln(nln(n))−1<p/n<ln(nln(n))，参见https://en.wikipedia.org/wiki/Prime-counting_function
# 得到上界后用挨拉托色尼筛法


def prime_list(n):
    # 前n个素数列表，注意此函数与problem3中的稍有不同
    l = [2, 3]
    i = 5
    length = 2
    while True:  # 大于3的素数必为奇数
        if length >= n:
            break
        for j in l:
            if j > round(math.sqrt(i)):  # 为防可能的程序计算精度误差，这里用一下round
                l.append(i)
                length += 1
                break
            if i % j == 0:
                break
        i += 2
        # 由伯特兰—切比雪夫定理易知p和p^2之间至少存在一个素数，故此else子句无必要，因为for循环中必然触发break
        # 伯特兰—切比雪夫定理说明：若整数n > 3，则至少存在一个质数p，符合n < p < 2n − 2
        # else:
        #     l.append(i)
    return l


print(prime_list(10001)[-1])
