# 1. 本程序求1-100整数中的奇数和，偶数和.

i = 0             # 2. 程序中直接定义整数为i,num1为奇数，num2为偶数.
num1 = 0
num2 = 0

while i <= 100:

    if i % 2 != 0:# if判断奇数，偶数
        num1 += i
    else:
        num2 += i
    i += 1
print("1-100之间奇数和为：%d" % num1)
print("1-100之间偶数和为 %d" %num2)
