

#input接收用户输入的数据是字符串类型，条件是age和整型18做判断，所以这里要用int转换数据类型

age=int(input('请输入你的年龄：'))

if age >= 18:
     print(f'你的年龄是{age}，你已成年，可以上网')
else:
    print(f'你未成年，小朋友，回家写作业去吧')
print('系统关闭')




#否则，会出现TyoeError
age=input('请输入你的年龄：')
if age >= 18 :
     print(f'你的年龄是{age}你已成年，可以上网')
else:
    print(f'你未成年，禁止上网')