#数字间的逻辑关系
a=0
b=1
c=2
#and运算符，只要有一个值为0则结果为0，否则结果为最后一个非0数字，全真才为真
print(a and b)#0
print(b and a)#0
print(a and c)#0
print(c and a)#0
print(b and c)#2
print(c and b)#1

#or运算符，只有所有值为0结果才为0，否则为第一个非0数字，全假才为假
print(a or b)#1
print(a or c)#2
print(b or c)#1
