#15.函数应用实战
import random
all_chars="0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
def generate_code(length=4):
    return ''.join(random.choices(all_chars, k=length))
print(generate_code())



def is_prime(num: int) -> bool:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

print(is_prime(7))
print(is_prime(15))

def gcd(x: int, y: int) -> int:
    """求最大公约数"""
    while y % x != 0:
        x, y = y % x, x
        print(x,y)
    return x
gcd(18,15)







"""
双色球随机选号程序

Version: 1.3
"""
import random

RED_BALLS = [i for i in range(1, 34)]
BLUE_BALLS = [i for i in range(1, 17)]


def choose():
    """
    生成一组随机号码
    :return: 保存随机号码的列表
    """
    selected_balls = random.sample(RED_BALLS, 6)
    selected_balls.sort()
    selected_balls.append(random.choice(BLUE_BALLS))
    return selected_balls


def display(balls):
    """
    格式输出一组号码
    :param balls: 保存随机号码的列表
    """
    for ball in balls[:-1]:
        print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
    print(f'\033[034m{balls[-1]:0>2d}\033[0m')


n = int(input('生成几注号码: '))
for _ in range(n):
    display(choose())




