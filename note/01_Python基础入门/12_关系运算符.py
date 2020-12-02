# 关系运算符用来比较两个值之间的关系，总会返回一个布尔值
# 如果关系成立，返回True，否则返回False
# >       比较左侧值是否大于右侧值
# >=      比较左侧值是否大于或等于右侧值
# <       比较左侧值是否小于右侧值
# <=      比较左侧值是否小于或等于右侧值
# ==      比较两个对象的值是否相等（比较的是值，不是对象id）
# !=      比较两个对象的值是否不相等（比较的是值，不是对象id）
# is      比较两个对象是否是同一个对象，比较的是对象的id
# is not  比较两个对象是否不是同一个对象，比较的是对象的id

result = 10 > 20 # False
result = 30 > 20 # True
result = 30 < 20 # False
result = 10 <= 10 # True
print('result : ' ,result)

# 在Python中可以对两个字符串进行大于（等于）或小于（等于）的运算
# 当对字符串进行比较是，实际上比较的是字符串的Unicode编码
# 并且在比较两个Unicode编码时，是逐位比较的，但是对于中文来说意义不是特别大
# 注意：如果不希望比较两个字符串的Unicode编码，则需要将其转换为数字然后再比较
result = '2' > '1' # True
print('result : ' ,result)
result = '2' > '11' # True
print('result : ' ,result)
result = 'a' > 'b' # False
print('result : ' ,result)
result = 'ab' > 'b' # False
print('result : ' ,result)
result = 'abc' > 'ab' # True
print('result : ' ,result)


result = 1 is True # False
print('result : ' ,result)

