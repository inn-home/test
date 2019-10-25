# 导入随机工具包
import random
player = int(input("请输入您要出的拳 石头（1）/剪刀（2）/布（3）"))
computer = random.randint(1,3)

print("玩家出拳是 %d - 电脑出拳是 %d" % (player,computer))
if ((player == 1 and computer == 2)
    or (player == 2 and computer ==3)
    or (player == 3 and computer ==1)):
    print("电脑弱爆了")
elif player == computer:
    print("很荣幸能够和你旗鼓相当"
          )
else:
    print("不服气，我们再来啊")