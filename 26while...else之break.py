i=1
while i<=5:
    if i==3:
        break#第三遍时终止，即只打印2遍

    print('媳妇儿，我错了')
    i+=1
else :
    print('媳妇儿原谅我了')
    #如果break执行表示循环非正常结束，此时不执行else之后的代码