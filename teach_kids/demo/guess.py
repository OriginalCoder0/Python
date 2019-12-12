import random

target = random.randint(1, 10)
guess = int(input("1~10之间猜一个数字："))

while guess != target:
    if guess > target:
        print(guess, "太大了")
    elif guess < target:
        print(guess, "太小了")

    guess = int(input("再猜一遍："))

print("猜对了！{} 是正确的数字".format(guess))
