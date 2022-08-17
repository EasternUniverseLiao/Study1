#引用能当做实际参数吗？
#可以，以下代码可以解释

def test1(a):
    print(a)
    print(id(a))

    a += a

    print(a)
    print(id(a))

#int :计算前后id不同
b = 1
test1(b)


#list:计算前后id相同
c = [11,22]
test1(c)

#以上实验表明无论是可变还是不可变的数据类型，都能当做实参