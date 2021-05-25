# About Year，Month，Week，Leap year，Century
import time


def is_leap_year(n):
    if n % 4 == 0:
        if n % 100 != 0 or n % 400 == 0:
            return True
    return False


def main1():
    l = []
    for i in range(1901, 2001):
        if is_leap_year(i):
            l.extend([31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])
        else:
            l.extend([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])

    s = 2
    count = 0
    for i in l[:-1]:  # 最后一个月的天数不能加上
        if s % 7 == 0:
            count += 1
            # print(s)
        s += i

    print(s)
    print(count)


def main2():
    l = []
    s = 2  # 1901年1月1日为星期二
    count = 0
    for year in range(1901, 2001):
        # 因为下面的for m, day循环时先执行循环体最后才s += day，所以2000年的最后一个月的day自然无用
        # if year == 2000:
        #     months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30] # 最后一个月天数不计
        if is_leap_year(year):
            months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        for m, day in enumerate(months):  # 最后一个月的天数不能加上
            # if year == 1901:
            #     print(s, s % 7, year, m + 1, 1)
            if s % 7 == 0:
                count += 1
                identify_day = time.strftime('%w', time.strptime(f'{year}-{m + 1}-{1}', '%Y-%m-%d'))
                print(s, year, m + 1, 1, identify_day)  # m+1才是month
            s += day

    print(s)
    print(count)


main1()
main2()
