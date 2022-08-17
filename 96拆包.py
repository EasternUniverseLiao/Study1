#在字典的学习中提到过拆包，就是把元素都遍历一遍

#1·拆包元组
def return_num() :
    return 1,2

num1,num2=return_num()
print(num1)
print(num2)

#2·字典拆包
dict1={'name':'Tom','age':18}
a,b=dict1#整出来的是keys
print(a)#name
print(b)#age

#要想得到Tom，18
print(dict1[a])
print(dict1[b])