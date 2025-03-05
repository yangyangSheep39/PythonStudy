# 所谓的类型转换，就是将一个类型的对象转换为另一个对象
# Python是强类型语言，类型转换不是改变对象本身的类型，而是将对象的值转换为新的对象
# 类型转换的四个函数  int()  float()  str()  bool() 

# int() 可以用来将其他的对象转换为整型
# 规则：
#       布尔值：True → 1   False → 0
#       浮点数：直接取整，省略小数点后的内容
#       字符串：合法的整数字符串，直接转换为对应的数字，如果不是合法的整数字符串，则报错 ValueError: invalid literal for int() with base 10: 'ha哈哈哈哈哈'
#       对于其他不可转换为整型的对象，直接抛出异常  ValueError
# int() 函数不会对原来的变量产生影响，他是将对象转换为指定的类型并将其作为返回值返回
# 如果希望修改原来的变量，则需要对变量进行重新赋值
# 可以在转换的时候指定int的进制
a = True
int(a)
print("a = ",a)
print("a的类型是：",type(a))
a = 11.6
print(int(a))
a = '123456'
print(int(a))
# a = 'ha哈哈哈哈哈'
print(int(a))
num = '1a'
print('16进制的1a =',int(num,16))
# a = None
# print(int(a))

# float() 可以用来将其他的对象转换为浮点数类型
print(float(a))
# str() 可以用来将其他的对象转换为字符串类型

# bool() 可以用来将其他的对象转换为布尔值类型，在Python中任何对象都可以转换为布尔值
# 对于所有的表示空性的对象都会转换为   False，其余的转换为   True
# 		哪些表示为空性：0、None、''......
'''
在python中，能够解释为假的值有：
None、0、0.0、False、
所有的空容器（空列表、空元组、空字典、空集合、空字符串）
'''
b = None
print(bool(b))
c = ''
print(bool(c))
