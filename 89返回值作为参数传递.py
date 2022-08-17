def test1():
    return 50

def rest2(num):
    print(num)

#1.保存函数test1的返回值
result=test1()

#2.将函数返回值所在变量作为参数传递到test2函数
rest2(result)#50