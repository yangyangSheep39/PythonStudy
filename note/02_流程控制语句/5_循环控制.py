"""break 用来退出循环"""
from types import new_class

num = 0
while num < 5:
    print("hello python", num)
    num += 1
    break

# 质数判断
n = 11
a = 2
flag = True
while a < n:
    if n % a == 0:
        print(n, "不是质数")
        flag = False
        break
    a += 1
if flag:
    print(n, "是质数")

n = 11
flag = True
for i in range(2, n):
    if n % i == 0:
        print(n, "不是质数")
        flag = False
        break
else:
    print(n, "是质数")

"""continue 跳过本次循环后面的剩余语句，然后继续下一次循环
注意：只能跳过距离最近的for或者while循环，中止一次"""
for i in range(5):
    if i == 2:
        continue
    print(i)

"""与else结合 else的下级代码：没有通过 break 退出循环，循环结束后，会执行的代码"""
n = 11
flag = True
for i in range(2, n):
    if n % i == 0:
        print(n, "不是质数")
        flag = False
        break
else:
    print(n, "是质数")

"""pass 当语句要求不希望任何命令或代码来执行时使用
说明：pass语句表示一个空操作，在执行时没有任何的响应，
pass的位置最终应该有代码来执行，只不过暂时写不出来
可以使用在流程控制和循环语句中"""
if 1:
    pass

# 指数爆炸 后一个是前一个的两倍
new_list = []
n = 0.1
w = n
for i in range(50):
    w *= 2
    new_list.append(w)
print(new_list)

# 国王麦粒
g = 1  # 当前格子的麦粒数量
total = 0  # 总的麦粒数量
a = 1  # 棋盘格子的序列
while a <= 100:
    total += g  # 计算当前的总麦粒数
    print('在放满了%d个格子以后，总的麦粒数是%d' % (a, total))
    a += 1  # 走到下一个格子
    g *= 2  # 当前格子应该放的麦粒数*2

# 人生的复利公式 (1+0.1=1.01)
day = 0
total = 1
while day < 3:
    total = total * 1.01
    print(total)
    day += 1
