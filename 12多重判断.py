#多重判断
age=int(input('请输入你的年龄:'))#输入数据并保存变量并改数据类型
if age<18:
    print(f'你输入的年龄是{age}，童工')


elif 18<=age<=60:#也可写成(age>=18)and(age<=60)
    print(f'你输入的年龄是{age}，为合法工作年龄')



elif age>60 :
    print(f'你输入的年龄为{age}，为退休年龄')


