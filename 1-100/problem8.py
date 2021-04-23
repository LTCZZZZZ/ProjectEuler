import numpy

digits = '''73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450'''

# 先删除换行符
digits = list(map(int, filter(lambda x: x not in ['\n', ], list(digits))))


def func1(m):
    # 程序虽然看起来复杂，但却是计算量最小的方式，尤其是当m很大的时候，运行时长会差别很大

    def find_not_zero(k):
        # 先找到一个不为0的位置
        i = k
        for i in range(k, len(digits) - m):
            temp = digits[i:i + m]
            if 0 not in temp:
                break
        return i

    def find_max_product(k):
        # 对当前这一段，找到最大积，如果碰到0，则return
        intermediate = 1  # 中间乘数
        max_i = i = k
        while i < len(digits) - m:
            a = digits[i]  # 在当前程序条件下，a不可能为0
            b = digits[i + m]
            if b == 0:
                break

            if a <= b:
                if i == max_i:
                    max_i += 1
                else:
                    intermediate *= b / a
                    if round(intermediate, 3) >= 1:  # 用round是为了避免可能存在的计算精度问题
                        max_i = i + 1
                        intermediate = 1  # 重置intermediate为1
                    else:  # 加上下面这两行是为了使逻辑结构看起来更清晰
                        pass
            elif a > b:
                intermediate *= b / a
            # i自增1，进入下一轮循环
            i += 1
        max_product = numpy.prod(digits[max_i:max_i + m])  # 特别注意：numpy.prod在使用整数类型时有溢出风险
        return max_i, max_product, i

    max_product_list = []  # 对每一个不为0的段，有一个max_product
    max_i_list = []
    i = find_not_zero(0)  # 记录当前乘积最大时的i
    while i < len(digits) - m:
        max_i, max_product, i = find_max_product(i)
        # 下面分成两段是为了好求最大值
        max_product_list.append(max_product)
        max_i_list.append(max_i)
        if i < len(digits) - m:
            i = find_not_zero(i + m + 1)  # 因为digits[i + m] = 0

    max_product = max(max_product_list)
    # print(max_product_list.index(max_product))
    max_i = max_i_list[max_product_list.index(max_product)]
    print(max_product, digits[max_i:max_i + m])


func1(4)
func1(13)
