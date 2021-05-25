import numpy as np


def main():
    s = np.math.factorial(100)
    # print(sum(map(int, list(str(s)))))
    print(sum(map(int, str(s))))  # 注意，list可以省略


main()
