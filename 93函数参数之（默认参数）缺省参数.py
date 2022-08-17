'''
缺省参数也叫默认参数，用于定义函数，为参数提供默认值，调用函数时可不传该默认参数的值，注意：
所有位置参数都必须在默认参数前，包括函数定义和调用。

'''

def user_info(name,age,gender='男') :
    print(f'您的名字是{name}，年龄是{age}，性别是{gender}')

user_info('Tom',age=20)#您的名字是Tom，年龄是20，性别是男
user_info('rose',18,'女')#您的名字是rose，年龄是18，性别是女