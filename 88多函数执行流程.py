# 1. 定义全局变量
glo_num = 0
def test1() :
    global glo_num
    # 修改全局变量
    glo_num = 100

def test2() :
    # 调用test1函数中修改后的全局变量
    print(glo_num)

# 2.调用test1函数，执行函数内部代码：声明和修改全局变量
test1()
# 3.调用test2函数，执行函数内部代码：打印
test2()  #100
