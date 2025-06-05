prices = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}
# 用股票价格大于100元的股票构造一个新的字典
prices2 = {key: value for key, value in prices.items() if value > 100}
print(prices2)



# 既想要访问元素的内容，又想知道它的位置（索引）
names = ['关羽', '张飞', '赵云', '马超', '黄忠']
courses = ['语文', '数学', '英语']
# 录入五个学生三门课程的成绩
# 错误 - 参考http://pythontutor.com/visualize.html#mode=edit
# scores = [[None] * len(courses)] * len(names)
scores = [[None] * len(courses) for _ in range(len(names))]
for row, name in enumerate(names):
    for col, course in enumerate(courses):
        scores[row][col] = float(input(f'请输入{name}的{course}成绩: '))
        print(scores)

#数据结构和算法
def select_sort(items, comp=lambda x, y: x < y):  #参数 comp 是一个比较函数，默认是 lambda x, y: x < y，即默认按从小到大排序。这个设计使得排序更灵活，比如你可以传入别的比较函数，实现降序或自定义排序。
    """简单选择排序"""
    items = items[:] #这里用切片复制了一份列表，避免修改原始 items
    for i in range (len(items)-1):
        min_index=i
        for j in range (i+1,len(items)):
            if comp(items[j],items[min_index]):
                min_index=j
        items[i],items[min_index]=items[min_index],items[i]
    return items
a=[6,4,5,3,8,2]
select_sort(a)

def bubble_sort(items, comp=lambda x, y: x < y):
    items = items[:]
    for i in range (1,len(items)):
        swapped=False
        for j in range (len(items)-i):
            if comp(items[j+1],items[j]):
                items[j],items[j+1]=items[j+1],items[j]
                swapped=True
        if swapped==False:
            break
    return items

 bubble_sort(a)

def merge(items1, items2, comp=lambda x, y: x < y):
    items=[]
    index1=0
    index2=0
    while index1<len(items1) and index2<len(items2):
        if comp(items1[index1],items2[index2]):
            items.append(items1[index1])
            index1+=1
        else:
            items.append(items2[index2])
            index2+=1
    items += items1[index1:]
    items += items2[index2:]
    return items
a=[1,3,5,7]
b=[2,4]
merge(a,b)

def bin_search(items, key):
    start=0
    end=len(items)-1
    while start<=end:
        mid = (start + end) // 2
        if items[mid]<key:
            start=mid+1
        elif items[mid]>key:
            end=mid-1
        else:
            return mid
    return -1

a=[1,3,5,7,13,23,34,42,55]
bin_search(a,23)

def  dynamic(items):
    partial=overall=items[0]
    for i in range(1,len(items)):
        partial=max(items[i],partial+items[i])
        overall=max(partial,overall)
    return overall

a=[-2, 1, -3, 4, -1, 2, 1, -5, 4]
dynamic(a)







from functools import wraps
from threading import RLock


def singleton(cls):
    """线程安全的单例装饰器"""
    instances = {}
    locker = RLock()

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:        # 第一次快速检查
            with locker:                # 开始排队！
                if cls not in instances:    # 轮到我时再检查一次
                    instances[cls] = cls(...)  # 只有我在创建
        return instances[cls]
    
'''
1. 对象的复制（深拷贝 vs 浅拷贝）
什么是拷贝？
拷贝就是复制一个对象，创建一个新的副本。
浅拷贝（Shallow Copy）
只复制对象的第一层，内部的对象仍然是引用

'''
import copy

# 原始数据
original = [1, 2, [3, 4]]

# 浅拷贝
shallow = copy.copy(original)
# 或者用切片
shallow = original[:]

print("原始:", original)    # [1, 2, [3, 4]]
print("浅拷贝:", shallow)   # [1, 2, [3, 4]]

# 修改浅拷贝的简单元素
shallow[0] = 999
print("修改后原始:", original)    # [1, 2, [3, 4]] - 没变
print("修改后浅拷贝:", shallow)   # [999, 2, [3, 4]] - 变了

# 修改浅拷贝的内部列表
shallow[2][0] = 888
print("修改内部后原始:", original)    # [1, 2, [888, 4]] - 也变了！
print("修改内部后浅拷贝:", shallow)   # [999, 2, [888, 4]] - 变了

'''
原始列表:     [1, 2, 指针→[3, 4]]
            ↓ 浅拷贝
浅拷贝列表:   [1, 2, 指针→[3, 4]]  (指向同一个内部列表!)
'''
'''
深拷贝（Deep Copy）
完全复制所有层次的对象，创建完全独立的副本
'''
import copy

# 原始数据
original = [1, 2, [3, 4]]

# 深拷贝
deep = copy.deepcopy(original)

print("原始:", original)  # [1, 2, [3, 4]]
print("深拷贝:", deep)    # [1, 2, [3, 4]]

# 修改深拷贝的内部列表
deep[2][0] = 888
print("修改后原始:", original)  # [1, 2, [3, 4]] - 没变
print("修改后深拷贝:", deep)    # [1, 2, [888, 4]] - 变了


'''
2. 垃圾回收机制
什么是垃圾回收？
自动清理不再使用的内存，防止内存泄漏。
引用计数（Reference Counting）
每个对象都有一个计数器，记录有多少个变量指向它
'''
# 理解引用计数
import sys

a = [1, 2, 3]  # 创建列表，引用计数 = 1
print(sys.getrefcount(a))  # 显示引用计数（实际会多1，因为getrefcount也会引用）

b = a          # b也指向同一个列表，引用计数 = 2  
print(sys.getrefcount(a))

del b          # 删除b，引用计数 = 1
print(sys.getrefcount(a))

del a          # 删除a，引用计数 = 0，对象被回收


#引用计数的问题：循环引用
# 循环引用示例
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# 创建两个节点
node1 = Node(1)  # node1引用计数 = 1
node2 = Node(2)  # node2引用计数 = 1

# 创建循环引用
node1.next = node2  # node2引用计数 = 2
node2.next = node1  # node1引用计数 = 2

# 删除外部引用
del node1  # node1引用计数 = 1（还有node2.next指向它）
del node2  # node2引用计数 = 1（还有node1.next指向它）

# 现在两个对象互相引用，但外部无法访问
# 引用计数永远不会变成0，造成内存泄漏！

'''
标记-清除（Mark and Sweep）
解决循环引用问题的算法

标记阶段：从根对象开始，标记所有可以访问到的对象
清除阶段：删除所有没有被标记的对象
'''
# 标记-清除过程示意
# 假设有循环引用：A ←→ B，但没有外部引用

# 标记阶段：
# - 从全局变量、局部变量等根对象开始
# - 标记所有可以到达的对象
# - A和B都无法从根对象到达，所以不会被标记

# 清除阶段：
# - 删除所有没有标记的对象
# - A和B被删除，解决了循环引用
'''
分代收集（Generational Collection）
基于"大部分对象都是短命的"这个观察
'''
# Python将对象分为3代
# 第0代：新创建的对象
# 第1代：经历过一次垃圾回收的对象  
# 第2代：经历过多次垃圾回收的对象

import gc

# 查看各代的对象数量
print(gc.get_count())  
# gc.get_count() 返回的是三代对象各自的“分配与回收的计数器”，

# 它表示：自上次回收以来创建了多少个对象，不是当前有多少对象。

# 手动触发垃圾回收
gc.collect()

'''
3. 弱引用（Weak Reference）
什么是弱引用？
指向对象但不增加引用计数的引用方式

为什么有弱引用？
因为：

如果所有引用都增加引用计数，就有可能导致“对象永远不会被销毁”⚠️。

比如：

缓存、观察者模式中，你希望引用一个对象，但不想阻止它被垃圾回收；

弱引用就允许你“偷偷关注”一个对象，而不会阻止它被删除。


'''

import weakref
import gc

class MyClass:
    def __init__(self, value):
        self.value = value
    
    def __del__(self):
        print(f"对象 {self.value} 被删除")

# 创建对象
obj = MyClass("测试")

# 创建弱引用
weak_ref = weakref.ref(obj)

print("弱引用指向的对象:", weak_ref().value)  # 测试

# 删除强引用
del obj

# 现在对象被回收了
print("弱引用指向的对象:", weak_ref())  # None




#实例：弱引用打破循环引用

import weakref

class Parent:
    def __init__(self, name):
        self.name = name
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)
        child.parent = weakref.ref(self)  # 用弱引用！

class Child:
    def __init__(self, name):
        self.name = name
        self.parent = None
    
    def get_parent(self):
        if self.parent:
            return self.parent()  # 调用弱引用获取对象
        return None

# 使用
parent = Parent("爸爸")
child = Child("孩子")
parent.add_child(child)

print(child.get_parent().name)  # 爸爸

# 删除父对象
del parent#：删除变量 parent 的引用，这个名字是最后一个强引用，Python会在之后自动销毁实例对象。
print(child.get_parent())  # None，父对象已被回收


'''
魔法方法也叫双下方法，形如 __init__、__add__、__eq__ 等，
它们是 Python 中预定义的一种特殊方法，用来实现一些「底层行为」。
系统自动执行的程序
'''

# 自定义的对象能不能使用运算符做运算？

# ✅ 能，只要实现对应的魔法方法。
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

'''
❓ 自定义的对象能不能放到 set 中？能去重吗？

✅ 能，但你必须实现：

__hash__：告诉 Python 如何给对象生成哈希值。

__eq__：告诉 Python 如何判断两个对象是否相等。

否则你放了两个一模一样的对象进去，它们也会被当成不同的对象。

❓ 自定义的对象能不能作为 dict 的键？

✅ 同样依赖 __hash__ 和 __eq__。

❓ 自定义的对象能不能使用 with 上下文语法？

✅ 需要实现：

__enter__()

__exit__()

'''



'''
二、Mixin（混入类）
Mixin 是一种类，用来为其他类添加功能，但本身不是完整的类。
'''

# Mixin 是一种类，用来为其他类添加功能，但本身不是完整的类。
class SetOnceMappingMixin:
    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + ' already set')
        return super().__setitem__(key, value)

class SetOnceDict(SetOnceMappingMixin, dict):
    pass
# 这就是用 Mixin + 继承 组合出一个只允许设置一次键值的字典。

'''三、元类 & 单例模式
Python 中类是由 元类（metaclass） 控制生成的，默认元类是 type。'''
#定义一个元类，是一个控制类只生成一个实例的元类。这就是单例模式：全局只存在一个对象实例。
class SingletonMeta(type):
    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            with cls.__lock:
                cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance

# 无论是不是第一次创建，最后都返回缓存的实例。

# 保证只有一个实例存在。

#用法：
class President(metaclass=SingletonMeta):
    pass

p1 = President()
p2 = President()
assert p1 is p2  # 始终返回同一个对象

'''
面向对象设计原则

单一职责原则 （SRP）- 一个类只做该做的事情（类的设计要高内聚）
开闭原则 （OCP）- 软件实体应该对扩展开发对修改关闭
依赖倒转原则（DIP）- 面向抽象编程（在弱类型语言中已经被弱化）
里氏替换原则（LSP） - 任何时候可以用子类对象替换掉父类对象
接口隔离原则（ISP）- 接口要小而专不要大而全（Python中没有接口的概念）
合成聚合复用原则（CARP） - 优先使用强关联关系而不是继承关系复用代码
最少知识原则（迪米特法则，LoD）- 不要给没有必然联系的对象发消息
说明：上面加粗的字母放在一起称为面向对象的SOLID原则。
'''


'''
策略模式 (Strategy Pattern)
你给的代码示例体现了策略模式：

策略模式：定义一系列算法（策略），让它们可以互换，客户端可以动态选择算法。
'''


class StreamHasher:
    """哈希摘要生成器"""

    def __init__(self, alg='md5', size=4096):
        self.size = size
        alg = alg.lower()
        # 动态导入hashlib模块，调用对应的算法构造函数
        self.hasher = getattr(__import__('hashlib'), alg)()

    def __call__(self, stream):
        return self.to_digest(stream)

    def to_digest(self, stream):
        """生成十六进制形式的摘要"""
        # 以 self.size 大小分块读取文件流
        for buf in iter(lambda: stream.read(self.size), b''):
            self.hasher.update(buf)  # 更新摘要
        return self.hasher.hexdigest()  # 返回最终摘要字符串


def main():
    hasher1 = StreamHasher()  # 默认 md5
    with open('Python-3.7.6.tgz', 'rb') as stream:
        print(hasher1.to_digest(stream))

    hasher2 = StreamHasher('sha1')  # sha1 算法
    with open('Python-3.7.6.tgz', 'rb') as stream:
        print(hasher2(stream))  # __call__方法被调用
