from problem18 import handle, func1


with open('p067_triangle.txt') as f:
    text = f.read()


d = handle(text)
# print(d)
print(func1(d))
