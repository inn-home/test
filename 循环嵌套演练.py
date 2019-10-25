# 定义初始值
days = 1
daytime = 3
night = 2
length = 0
while length <= 10:
    # 若条件不满足7，则算日长度+总长度
    length = length + daytime
    if length > 10:
        break
        # 条件满足跳出循环，执行下一种情况
    else:
        length = length - night
        days = days + 1
print("%d" % days)


