'''
Description: 
Autor: yangyangSheep
Date: 2021-01-18 16:31:55
LastEditors: yangyangSheep
LastEditTime: 2021-01-18 17:48:42
'''
# 条件判断语句(if语句)
# 语法:
# 	 if 条件表达式 : 语句
# 执行流程:if语句在执行时，会相对条件表达式进行求值判断
# 	如果为True，则执行if后的语句
# 	如果为False，则不执行
# 默认情况下:if语句  只会控制紧随其后的那条语句
# 	如果希望if可以控制多条语句，则可以在if后跟着一个代码块
# 	如果要编写代码块，语句就不能紧随在 : 后边，而是要写在下一行
#
#
# 代码块:
# 		代码块中保存着一组代码，同一个代码块中，要么都执行，要么都不执行
# 		代码块就是一种为代码分组的机制
#
if True: print("True会执行")
if False: print("False不会执行")

num = 20
if num > 10: print("num比10大")
print('此条未被if控制')

if True:
    print('123')
    print('代码块内受if控制')
print('不受控制')

num = 18
if num > 10:
    print("num比10大，并且num比20小")

# 逻辑判断符
num = 28
if num > 10 and num < 20:
    print("num比10大，并且num比20小")

'''双分支
if 和 else 语句以及各自的缩进部分共同是一个 完整的代码块'''
weather = '下雨'
if weather == '下雨':
    print('出门要带伞')
else:
    print('戴个帽子')

'''多分支
使用if 可以 判断条件使用 else 可以处理 条件不成立的情况
但是，如果希望 再增加一些条件，条件不同，需要执行的代码也不同时，
就可以使用 elif'''
score = 98
if score > 90:
    print('A')
elif 80 < score < 90:
    print('B')
elif 70 < score < 80:
    print('C')
else:
    print('D')
