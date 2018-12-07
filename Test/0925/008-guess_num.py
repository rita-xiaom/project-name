#猜数字游戏

#生成随机数
import random
answer=random.randint(1,100)
#玩家输入数字
n=int(input('please input num(1-100): '))
#判断输入数字大小
while n!=answer:
    if n>answer:
        n=int(input('Num is more,Please continue input num: '))
    elif n<answer:
        n=int(input('Num is lesss,Please continue input num: '))
#输入正确，游戏结束
print("you win the game!")