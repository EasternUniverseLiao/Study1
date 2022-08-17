i=1
while i<=5:
    if i==3 :
        i+=1
        continue
    print('媳妇儿，我错了')
    i+=1
else :
    print('媳妇儿原谅我了')
    #与break不同的，只终止第三次，循环任然正常结束，故可以打印else后的代码
