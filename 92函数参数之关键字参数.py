'''
函数调用，通过键=值的形式加以指定，可以让函数更清晰，容易使用，同时也消除了顺序的需求

'''

def user_info(name,age,gender) :
    print(f'您的名字是{name}，年龄是{age}，性别是{gender}')

user_info('Tom',gender='男',age=20)
#注意：有位置参数时要把位置参数放在关键字参数的前面，但关键字参数之间不存在先后顺序。
