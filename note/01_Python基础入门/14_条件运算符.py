# 条件运算符（三元表达式）
# 语法： 语句1 if 条件表达式 else 语句2
# 执行流程：
# 		条件运算符在执行时，会先对条件表达式进行求值判断
# 		如果判断结果为True，则执行语句1，并返回执行结果
# 		如果判断结果为False，则执行语句2，并返回执行结果

print('hello') if False else print('你好')

a = 10
b = 20 
print('a的值比较大！') if a > b else print('a的值比较小！')


max  =  a if a > b else b
print(max)

# 通过条件获取三个值中最大的值
x = 30
y = 40 
z = 50
max = x if x > y else y
max = max if max > z else z
print(max)

max = x if x > y and x > z else y if y > z else z
print(max)