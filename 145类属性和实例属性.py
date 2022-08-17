"""
1.设置类属性的方法
2.访问类属性的方法
3.修改类属性的方法
"""


class Dog(object):
    """创建狗类"""
    tooth = 10  # 设置类属性


# 类属性的归属者是类

wangcai = Dog()
xiaohei = Dog()

print(Dog.tooth)  # 10通过类访问类属性
print(wangcai.tooth)  # 10通过对象访问类属性
print(xiaohei.tooth)  # 10通过对象访问类属性

"""类属性的优点：记录的某项数据始终保持一致，为了节省内存空间，就定义类属性"""

# 不能通过对象修改类属性，如果硬要这样操作，实际上是创建了一个同名的实例属性
wangcai.tooth = 20
print(Dog.tooth)  # 12
print(wangcai.tooth)  # 20
print(xiaohei.tooth)  # 12
