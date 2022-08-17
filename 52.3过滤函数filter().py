list1 = list(range(-5,5))
print(list1)#[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
#
# list2 = list(filter(lambda i:i>0,range(-5,5)))
# print(list2)


list2 = list(filter(lambda i: i > 0, list1))#关于lambda后面会讲解

print(list2)