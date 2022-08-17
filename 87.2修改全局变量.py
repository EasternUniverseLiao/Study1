a = 100
print(a)   #100


def testA() :
    print(a)   #访问全局变量a，并打印变量a的存储的数据


def testB() :
    a=200     #局部修改不会对全局变量造成影响，但是如果直接修改，此时的testB函数访问的的a变量是局部变量
    print(a)  # 访问修改后的变量a，并打印变量a的存储的数据
'''
如果想要在函数体内部修改全局变量，那么就要：
#global 关键字声明a是全局变量
    global a
    a = 200   #这里修改的a是全局变量
    print(a)

经过了这个函数，会把全局变量a改变    

'''



testA()   #100


testB()   #200

print(a)
