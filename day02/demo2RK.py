import random
if __name__ == '__main__':

    num = 0
    num = input("输入")

    num=int(num)

    a = random.choice(range(10))
    a= int(a)

    if a > num :
        print("a">"num")
