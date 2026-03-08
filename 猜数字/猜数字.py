"""
猜数字的游戏
"""
import random
num = random.randint(1,10)
while True:
    #循环保证游戏进行
    guess = int(input("输入数字："))
    #将用户输入数据放进循环里面，确保不会进入死循环
    if guess == num:
        print("你猜对了")
        break
        #break退出循环
    elif guess > num:
        print("猜大了")
    else:
        print("猜小了")
