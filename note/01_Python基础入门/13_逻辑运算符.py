# 逻辑运算符
# 	主要用来做一些逻辑判断
# not  逻辑非（一元运算符【运算符两侧只有一个数据】可以对符号右侧的值进行非运算）
# 	布尔值：取反操作
# 	非布尔值：非运算会先将其转换为布尔值，然后再取反
a = True
a = not a
print('a = ', a)

a = 1
a = not a
print('a = ', a)
# and  逻辑与（二元运算符，可以对符号两侧的值进行与运算）
# 	要求只有在符号两侧的值都为True时，才会返回True，只要有一个False就返回False
# 	Python中的与运算时短路与，是去找False进行判断的，如果第一个值为False，则不会再进行后续的判断
a = True and True # True
print('a = ', a)
a = True and False # False
print('a = ', a)
a = False and True # False
print('a = ', a)
a = False and False # False
print('a = ', a)

True and print('我第一个值是True，不会短路')
False and print('我第一个值是False，会短路')
# or   逻辑或（可以对符号两侧的值进行或运算）
# 	两个值中只要有一个True就返回True
# 	Python中的或运算时短路或，是去找True进行判断的，如果第一个值为True，则不会再进行后续的判断
a = True or True # True
print('a = ', a)
a = True or False # True
print('a = ', a)
a = False or True # True
print('a = ', a)
a = False or False # False
print('a = ', a)
True or print('我第一个值是True，会短路')
False or print('我第一个值是False，不会短路')


# 非布尔值的与或运算
# 	当我们对非布尔值进行与或运算时，Python会将其当作布尔值运算，最终会返回原值
# 	与运算的规则
# 		与运算是找False的，如果第一个值是False，则不看第二个值
# 		如果第一个值是False，则直接返回第一个值，否则返回第二个值
# 	或运算的规则
# 		或运算是找True的，如果第一个值是True，则不看第二个值
# 		如果第一个值是True，则直接返回第一个值，否则返回第二个值
# True and True
result = 1 and 2  # 2
print(result)
# True and False
result = 1 and 0  # 0
print(result)
# False and True
result = 0 and 1  # 0
print(result)
# False and False
result = 0 and None  # 0
print(result)
result = 1 and None  # None
print(result)