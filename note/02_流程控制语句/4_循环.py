"""while循环"""
from sys import flags

num = 0
while num < 5:
    print("hello python", num)
    num += 1

# 高斯求和
n = 1
result = 0
while n < 101:
    result += n
    n += 1
print(result)

"""for 循环"""
for i in range(10):
    print("hello", i)

# range 函数，迭代器，生成一个list
print(list(range(10)))
# 阶乘
n = 4
result = 1
for i in range(n + 1):
    if i > 0:
        result *= i
print(result)