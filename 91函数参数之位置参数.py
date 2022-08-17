'''位置参数

'''
def user_info(name,age,gender) :
    print(f'您的名字是{name}，年龄是{age}，性别是{gender}')

user_info('Tom',20,'男')
#user_info('Tom',20)#个数定义和传入不一样会报错：TypeError: user_info() missing 1 required positional argument: 'gender'


#注意传递和定义参数的顺序及个数要一致