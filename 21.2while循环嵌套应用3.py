#以下是自己尝试
j=1
while j<=9:
    i=1
    while i<=j:#使i与j发生联动
        k=i*j
        print(f'{i}*{j}={k}', end='\t')#不修改默认会导致分行打印*
        i+=1
    print()#调用空的print，利用print默认自带换行，为了让每五个*换行
    j+=1




#课程
'''
1打印一个表达式
2一行打印多个表达式--行数和表达式数相等
3打印多行表达式
'''
j=1
while j<=9 :
    i=1
    while i<=j :#使i与j发生联动
        print(f'{i}*{j}={i*j}',end='\t')
        i+=1
    print()#调用空的print，利用print默认自带换行，为了让每五个*换行
    j+=1
