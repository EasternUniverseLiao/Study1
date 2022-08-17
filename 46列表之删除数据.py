#1 del
list1=['Tom','Lily','Rose']
del list1
print(list)
'''
也可以
del(list1)
'''
list1=['Tom','Lily','Rose']
del list1[1]#也可以删除指定下标数据
print(list1)

#2 .pop()------删除指定下标数据，如果不指定下标，默认删除最后一个数据，删除后可用新变量接收,删除后新变量返回被删的数据
list1=['Tom','Lily','Rose']
del_name = list1.pop(1)#不写下标默认删最后
print(del_name)
print(list1)


#3 .remove(数据)
list1=['Tom','Lily','Rose']
list1.remove('Tom')#移除'Tom'第一个这个数据
print(list1)
#4  .clear()-----清空
list1=['Tom','Lily','Rose']
list1.clear()
print(list1)

