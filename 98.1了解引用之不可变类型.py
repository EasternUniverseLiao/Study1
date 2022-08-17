#引用：在python中，值都是靠引用来传递的,可以理解为IP地址，或变量名
a = 1
b = a
print(b)

print(id(a))#十进制地址1701226416
print(id(b))#1701226416

a = 2

print(id(a))#1701226432
print(id(b))#1701226416
#整型数据类型不可变