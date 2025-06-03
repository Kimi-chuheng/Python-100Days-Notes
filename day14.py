#14.函数和模块
"""
输入m和n，计算组合数C(m,n)的值

"""
def stage(x):
    result=1
    for i in range(1,x+1):
        result*=i
    return result

m=int(input("m="))

n=int(input("n="))
y=stage(m)/stage(n)/stage(m-n)
print(y)

