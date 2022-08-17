'''
变量作用域指的是变量生效的范围，主要分两种：局部变量和全局变量。


局部变量：所谓局部变量是定义在函数体内部的变量，即只在函数体内部生效。

def testA():
    a = 100
    print(a)
testA()  #100
print(a)   #NameError: name 'a' is not defined

变量a是定义在testA函数内部的变量，在函数外部访问直接报错。

局部变量的作用：在函数体内部，临时保存数据，即当函数调用完成后，则销毁局部变量。

全局变量：所谓全局变量，指的是在函数体内、外部都能生效的变量。

a = 100
print(a)   #100
def testA() :
    print(a)   #访问全局变量a，并打印变量a的存储的数据
def testB() :
    print(a)   #访问全局变量a，并打印变量a的存储的数据
testA()   #100
testB()   #100

'''



'''
函数的闭包：






'''
def f1():
    x = 100
    def f2():
        print(x)
    return f2()#这里不能少

f1()#即使x 不是全局变量，但x被包在f1()里面



def y1(x):
    def y2(y):
        return x**y
    return y2#注意这里的写法
print(y1(2)(3))