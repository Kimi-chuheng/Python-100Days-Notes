#基本模式
# 文本模式
# 'r' - 只读模式（默认）
file = open('test.txt', 'r', encoding='utf-8')
content = file.read()  # 只能读取，不能写入
file.close()

# 'w' - 写入模式（会覆盖原文件）
file = open('test.txt', 'w', encoding='utf-8')
file.write('新内容')  # 原文件内容会被完全替换
file.close()

# 'a' - 追加模式
file = open('test.txt', 'a', encoding='utf-8')
file.write('追加的内容')  # 在文件末尾添加内容
file.close()

# 'x' - 创建模式（文件存在则报错）
file = open('new_file.txt', 'x', encoding='utf-8')
file.write('只有文件不存在时才能创建')
file.close()

# 二进制模式
# 'rb' - 二进制只读
file = open('image.jpg', 'rb')
data = file.read()  # 读取字节数据
file.close()

# 'wb' - 二进制写入
file = open('copy.jpg', 'wb')
file.write(data)  # 写入字节数据
file.close()

# 'ab' - 二进制追加
file = open('data.bin', 'ab')
file.write(b'binary data')  # 追加字节数据
file.close()

# 组合模式
# 'r+' - 读写模式（文件必须存在）
file = open('test.txt', 'r+', encoding='utf-8')
content = file.read()    # 可以读取
file.write('追加内容')   # 也可以写入
file.close()

# 'w+' - 读写模式（会清空文件）
file = open('test.txt', 'w+', encoding='utf-8')
file.write('新内容')     # 先写入
file.seek(0)            # 移动到文件开头
content = file.read()    # 再读取
file.close()

# 'a+' - 追加读写模式
file = open('test.txt', 'a+', encoding='utf-8')
file.write('追加内容')   # 在末尾追加
file.seek(0)            # 移动到开头
content = file.read()    # 读取全部内容
file.close()

#异常处理
'''
try: 包含可能出错的代码
except: 处理特定异常，可以有多个
else: 只有在没有异常时才执行
finally: 无论是否有异常都会执行
raise: 主动抛出异常
'''
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    
    def withdraw(self, amount):
        try:
            # 验证输入
            if not isinstance(amount, (int, float)):
                raise TypeError("金额必须是数字")
            
            if amount <= 0:
                raise ValueError("金额必须大于零")
            
            if amount > self.balance:
                raise Exception("余额不足")
            
            # 执行操作
            self.balance -= amount
            print(f"成功提取 {amount} 元")
            
        except TypeError as e:
            print(f"类型错误: {e}")
            raise  # 重新抛出给调用者处理
            
        except ValueError as e:
            print(f"数值错误: {e}")
            
        except Exception as e:
            print(f"操作失败: {e}")
            
        else:
            print(f"当前余额: {self.balance}")
            
        finally:
            print("交易处理完成")

# 使用示例
account = BankAccount(1000)

# 正常提取
account.withdraw(200)

print("\n" + "="*30 + "\n")

# 异常情况
account.withdraw(2000)  # 余额不足
