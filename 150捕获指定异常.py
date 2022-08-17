'''异常类型
    NameError无定义
    SyntaxError
    ZeroDivisionError除数为0
    FileNotFoundError文件找不到
    ...






语法：
try:
    可能发生错误的代码（注意：一般只放一行代码）
except 错误类型:（注意：如果错误类型不一致，无法成功捕获）
    异常发生需要执行的代码

'''
try:
    print(num)
except NameError:
    print('有错误NameError')

try:
    print(1/0)
except ZeroDivisionError:
    print('有错误ZeroDivisionError')

