dict1 = {'name':'Tom','age':20,'gender':'男'}
print(dict1)


#修改
dict1['name'] = 'rose'
print(dict1)


#.undate(另一个字典):合并





#新增
dict1['id'] = '001'#给一个原本子典没有的序列
print(dict1)


#删除
#del或者.pop():不输入任何参数则默认删除最后一个，但字典是无序的，这就矛盾，导致报错！
'''del(dict1)
print(dict1)#会报错，先注释掉'''
dict1 = {'name':'Tom','age':20,'gender':'男'}
del dict1['name']#删除指定键值对，如果键值对不存在则会报错
print(dict1)


#clear
dict1 = {'name':'Tom','age':20,'gender':'男'}
dict1.clear()
print(dict1)



#查找
dict1 = {'name':'Tom','age':20,'gender':'男'}
print(dict1['name'])#如果查找没有的key，会报错
#get
#字典序列.get(key,默认值)
dict1 = {'name':'Tom','age':20,'gender':'男'}
print(dict1.get('name'))#Tom
print(dict1.get('id'))#如果key不存在则返回None
print(dict1.get('id','001'))#如果参数二被设置了，就可以查找到

#keys()
dict1 = {'name':'Tom','age':20,'gender':'男'}
print(dict1.keys())#dict_keys(['name', 'age', 'gender'])查找所有key，返回可迭代的对象

#values()
dict1 = {'name':'Tom','age':20,'gender':'男'}
print(dict1.values())#dict_values(['Tom', 20, '男'])查找所有值，返回的也是可迭代对象
#items()
dict1 = {'name':'Tom','age':20,'gender':'男'}
print(dict1.items())#dict_items([('name', 'Tom'), ('age', 20), ('gender', '男')]),返回的仍然是一个可迭代对象




