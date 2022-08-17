#else下方缩进的代码是指当循环结束时要执行的代码


i=1
while i<=5:
    print('媳妇儿，我错了')
    i+=1
print('媳妇儿原谅我了')#这个print是不是没有循环也能执行

i=1
while i<=5:
    print('媳妇儿，我错了')
    i+=1
else :
    print('媳妇儿原谅我了')