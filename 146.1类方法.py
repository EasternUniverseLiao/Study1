"""
需要用装饰器@classmethod标识为类方法，第一个参数必须是类对象，一般以cls作为第一个参数

当方法中需要使用类对象（如果访问私有类属性等）时，定义类方法
类方法一般和类属性配合使用
"""


class Dog(object):
    __tooth = 10

    @classmethod
    def get_tooth(cls):
        return cls.__tooth


wangcai = Dog()
result = wangcai.get_tooth()
print(result)  # 10
