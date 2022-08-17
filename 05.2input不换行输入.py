x,a,b,c,d=map(int,input().split())#类似于C++的cin和scanf

print(a+b+c+d+x)

#或者
a=input()
#将输入的字符串存为a
b,c=a.split(' ')
#之后以某种方式分开
print(b)
print(c)


#再或者
a,b,c=input().split()
print(a)#此时a接收的是字符串，要改需要数据类型转换，后面06会提到
print(b)
print(c)