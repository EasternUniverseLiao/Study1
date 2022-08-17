list1 = ['Tom','Lily','Rose']
list2 = list1.copy()#或者list2=list1[:]
'''
copy.copy是浅复制
copy.deepcopy是深复制
'''


print(list2)
print(id(list1))
print(id(list2))
'''list1.append('hahaha')
print(list1)
print(list2)
'''