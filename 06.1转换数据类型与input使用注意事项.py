#转换数据类型的函数
"""
int(x)                  将x转换为一个整数
float(x)                将x转换为一个浮点数
注意：python无单双精度之分，单精度：1位符号位，8位指数位，23位小数，共32位，平时单精度大约小数点后6位
                          双精度：1位符号位，11位指数位，52位小数，共64位，平时双精度大约小数点后15位

complex(x)              将x转换为复数

str(x)                  将x转换为一个字符串
tuple(s)                将序列s转换为一个元组
list（s）               将序列s转换为一个列表
set(s)                  将序列s转换为一个集合
eval(str)                用来计算在字串符中有效Python表达式，并返回一个对象
"""

print(complex(1))

num=input("请输入数字")

print(num)

print(type(num))#str(字符串）

print(type(int(num)))

print(type(float(num)))



