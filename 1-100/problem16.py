from functools import reduce

s = str(2 ** 1000)
print(sum(map(int, list(s))))
print(reduce(lambda x, y: int(x) + int(y), list(s)))
