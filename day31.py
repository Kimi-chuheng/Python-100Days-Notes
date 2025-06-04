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

