'''
符号为大括号
数据为“键值对”形式出现
各个键值对之间用逗号隔开
'''
dict1 = {'name':'Tom','age':20,'gender':'男'}
print(dict1)
print(type(dict1))


#创建空字典
#1
dict2 = {}
print(type(dict2))


#2
dict3 = dict()
print(type(dict3))


#3

a=(1,2,3)
dict4 = dict.fromkeys(a)
print(dict4)

#创建字典

keys=[1,2,3,4]
values=[1,4,9,16]
dict5=dict(zip(keys,values))
print(dict5)




