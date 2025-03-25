"""闰年判断
输入一个年份（大于 1582的整数），判断这一年是否是闰年，
如果是输出 1，否则输出0。
普通闰年的年份是4的倍数，且不是100的倍数；
世纪闰年的年份必是400的倍数。"""

year = int(input("请输入年份："))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('是闰年')
else:
    print('不是闰年')

# ==0可以简化写，在前面加not就好
if (not year % 4 and year % 100) or not year % 400:
    print('是闰年')
else:
    print('不是闰年')
