def func1():
    # 笨办法
    nums = []
    for i in range(999, 900, -1):
        for j in range(i, 900, -1):
            s = str(i * j)
            if s == s[::-1]:
                nums.append((i, j, s))
    print(nums)
    print(max(int(item[2]) for item in nums))


def func2():
    # 优化版
    """Next we should consider counting downwards from 999 instead of counting
    upwards from 100. This makes the program far more likely to find a large
    palindrome earlier, and we can quite easily stop checking a and b that would
    be too small to improve upon the largest palindrome found so far."""
    max_num = 0
    for i in range(999, 100, -1):
        for j in range(i, 100, -1):
            num = i * j
            if num <= max_num:
                break
            s = str(num)
            if s == s[::-1]:
                max_num = num
                print(i, j)

    print(max_num)


func1()
func2()
# 尚可进一步优化，因为此回文数必能被11整除，参见 https://projecteuler.net/overview=004
