#猜数游戏
#生成1-100的随机数
import random
answer=random.randint(1,100)
#玩家输入数值
n=int(input("please input the answer： "))
#判断该数值的大小，给出提示信息
while n!=answer:
    if n>answer:
        n=int(input("the answer is more,please contion input: "))
    if n<answer:
        n=int(input("the answer is less,please contion input: "))
#输入正确答案
print("you are right!")