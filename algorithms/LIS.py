# 最长递增子序列（longest increasing subsequence）


# 最常规想法
def func0(l):
    """计算出每个元素作为序列起始点的最长递增子序列的长度，然后比较，这应该是计算量最大的算法"""
    record = []  # 以l[i]作为起始元素的最长递增子序列的长度
    longest_list = []
    for i in range(0, len(l)):
        length = 1
        end_num = l[i]
        longest = [l[i]]
        for j in range(1, len(l) - i):
            if (temp := l[i + j]) >= end_num:
                end_num = temp
                length += 1
                longest.append(end_num)
        record.append(length)
        longest_list.append(longest)
    print(record)
    print(longest_list)
    temp = max(record)
    return temp, longest_list[record.index(temp)]


# Dynamic Programming 1
def func1(l):
    """dp[i] 表示以 l[i] 结尾的最长递增子序列长度。
    另外，这个算法的稳定性有待考量，即，在列表中存在相等元素时的处理情况"""
    dp = []
    longest_list = []
    for i in range(0, len(l)):
        if i == 0:
            dp.append(1)
            longest_list.append([l[i]])
        else:
            # print(i)
            lengths = []  # 可能的最大长度列表，为求longest，每次循环都得添加一个元素以一一对应，如果只求最大长度的话，则无需在else时添加，但初始值要改为[1]
            for j in range(0, i):
                if l[j] <= l[i]:
                    lengths.append(dp[j] + 1)
                else:
                    lengths.append(1)
            # 这两步可以优化，但没必要了
            temp = max(lengths)
            if temp == 1:
                longest = [l[i]]
            else:
                longest = longest_list[lengths.index(temp)].copy()
                longest.append(l[i])
            # print(lengths)
            # print(temp, lengths.index(temp))
            # print(longest)
            dp.append(max(lengths))
            longest_list.append(longest)
    print(dp)
    print(longest_list)
    temp = max(dp)
    return temp, longest_list[dp.index(temp)]


# Dynamic Programming 2
def func2(l):
    """dp[i] 表示长度为 i 的最长递增子序列（LIS）的最小的 末尾的数。
    比如l = [1, 3, 5, 7, 6, 2]，
    迭代到7的位置的时候(完成)，dp = [0, 1, 3, 5, 7]，
    但迭代到4的位置的时候，    dp = [0, 1, 3, 5, 6]，用6替换了7，
    而迭代到2的位置的时候，    dp = [0, 1, 2, 5, 6]，用2替换了3，
    因为此时长度为2的LIS"""
    dp = [0]  # dp[0] = 0无实际意义，主要是为了适配下面的程序逻辑，如任意l[i] > dp[0]，下面续
    for i in range(0, len(l)):  # 注意这里迭代序列中的i和上面注释中的i的含义并不相同
        if i == 0:
            dp.append(l[i])  # 当前长度为1的LIS末尾的数为l[i]
        else:
            for j in range(len(dp) - 1, -1, -1):  # 倒序遍历
                if l[i] > dp[j]:
                    if j == len(dp) - 1:
                        dp.append(l[i])
                    else:
                        # 任意l[i] > dp[0]，故而在l[i]比dp中所有元素(0除外)都小时会被置为l[1]
                        dp[j + 1] = l[i]
                    break  # 必不可少
                # l[i] < dp[j]时自动进入下一次循环

    print(dp)
    # 思考：这个算法怎样返回所求的LIS？
    return len(dp) - 1


# 额外思考：这个过程其实就类似于，将一条链转化为一颗树，然后求树的最长子树及其长度
# 转换逻辑：有点复杂，参考func2，感觉要维护一条待比较的链，即func2中dp，dp中的元素分散在树的各个位置，只是(相对于根节点的)级别各不相同
#
# 以这个方式再写一个函数如下
def chain_to_tree(l):
    pass



if __name__ == '__main__':
    l = [4, 2, 3, 1, 5]
    print(func0(l))
    print(func1(l))
    print(func2(l))
