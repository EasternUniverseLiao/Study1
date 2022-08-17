name = "TOM"
age = 18
id = 1
print("我的名字是%s,今年我的年龄是%d岁" % (name, age))
print(f'我的名字是{name},今年{age}岁了')
print('我的名字是{},今年{}岁了'.format(name, age))

print("{} 数字是 {{0}}".format("a"))#{}再加{}会使{}原本作用变更

print('{1} {0}'.format(name, age))  # 可以用下标指定输出顺序

# print('{}{}{}'.format(name,age))
print('{} {}'.format(name, age, id))  # format里参数只能多不能少



list1 = ['你好世界','我很高兴学习python']
print('{} '.format(list1))