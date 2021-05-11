import time
import functools


def timer(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        time1 = time.time()
        res = func(*args, **kwargs)
        time2 = time.time()
        print(f"执行时间：{time2 - time1}")
        return res

    return wrapper
