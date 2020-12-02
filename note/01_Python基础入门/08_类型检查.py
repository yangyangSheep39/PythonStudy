# 通过类型检查，可以检查指定值（变量--变量没有类型，即检查变量对应值的类型）的类型
a = 123
b = '123'
print ('a = ' ,a)
print ('b = ' ,b)

# type() 用来检查值的类型，该函数会将检查的结果作为返回值返回，可以通过变量来接收函数的返回值
c = type(123)
print (c)
c = type(a)
print (c)
print (type(b))

print(type(1))  # <class 'int'>
print(type(1.5))  # <class 'float'>
print(type(True))  # <class 'bool'>
print(type('hello'))  # <class 'str'>
print(type(None))  # <class 'NoneType'>