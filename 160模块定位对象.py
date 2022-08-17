"""
按照以下的顺序搜索

1 当前目录
2 如果不在当前目录，Python则搜索在shell变量PythonPath下的每个目录
3 如果找不到，Python会查看默认路径，默认路径一般为user/local/lib/python/

"""
# 重复带来的麻烦1
# 自己的文件名不能和已有的模块名重复
import random

num = random.randint(1, 5)
print(num)

# 如果创建了一个名叫random的py文件，并在random文件中调用这个模块就会报错


# 重复带来的麻烦2
from time import sleep

sleep(2)  # 在定义前调用不会影响
print("jjj")


def sleep():
    print("我是自定义的sleep")


sleep()  # 调用前有定义了sleep，优先调用自定义的函数
print('kkk')

# 重复带来的麻烦3
import time

print(time)  # <module 'time' (built-in)>
time = 1
print(time)  # 结果嘿嘿嘿，只可意会
# 为什么变量可以覆盖模块
# 答案：python语言中数据是通过（ 引 用 ） 传递的，后面的数据覆盖前面的引用

