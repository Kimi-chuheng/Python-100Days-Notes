#对象的序列化和反序列化
import json

my_dict = {
    'name': '骆昊',
    'age': 40,
    'friends': ['王大锤', '白元芳'],
    'cars': [
        {'brand': 'BMW', 'max_speed': 240},
        {'brand': 'Audi', 'max_speed': 280},
        {'brand': 'Benz', 'max_speed': 280}
    ]
}
print(json.dumps(my_dict))



my_dict = {
    'name': '骆昊',
    'age': 40,
    'friends': ['王大锤', '白元芳'],
    'cars': [
        {'brand': 'BMW', 'max_speed': 240},
        {'brand': 'Audi', 'max_speed': 280},
        {'brand': 'Benz', 'max_speed': 280}
    ]
}
with open('data.json', 'w') as file:
    json.dump(my_dict, file)

'''
dump - 将Python对象按照JSON格式序列化到文件中
dumps - 将Python对象处理成JSON格式的字符串
load - 将文件中的JSON数据反序列化成对象
loads - 将字符串的内容反序列化成Python对象

核心概念
序列化：对象 → 字节流/字符串/文件
反序列化：字节流/字符串/文件 → 对象
为什么需要序列化？
程序运行时，对象存在内存中，但内存是易失的：

存储需求：将对象保存到硬盘文件
网络传输：在不同程序/计算机间传递数据
进程通信：不同进程间交换对象
'''


with open('data.json', 'r') as file:
    my_dict = json.load(file)
    print(type(my_dict))
    print(my_dict)


#使用网络API获取数据
#pip install requests
import requests

API_KEY = "f2004af9bd16e2538af2d716c036e272"  # 官方提供的演示 key，每分钟有请求次数限制
url = f"https://gnews.io/api/v4/top-headlines?lang=zh&country=cn&token={API_KEY}"

response = requests.get(url)
data = response.json()

# 检查返回结果
if "articles" in data:
    for article in data["articles"]:
        print("📰", article["title"])
        print("📅", article["publishedAt"])
        print("🔗", article["url"])
        print("-" * 60)
else:
    print("API 返回异常，内容如下：")
    print(data)
