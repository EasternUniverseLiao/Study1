#分析：打印呈三角形形状的*，每行*个数和行数相等
j=0
while j<5 :
    i=0
    while i<=j:#使i与j发生联动
        print('*', end='')#不修改默认会导致分行打印*
        i+=1
    print()#调用空的print，利用print默认自带换行，为了让每五个*换行
    j+=1
