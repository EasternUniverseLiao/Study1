#方法一:借用另一个变量暂存
a = 10
b = 20
c = 0
c = a
a = b
b = c
print(a,b)#20 10

#方法2
a , b = 1 , 2
a , b = b , a
print(a,b)#2 1