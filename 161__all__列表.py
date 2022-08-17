# __all__限制导入

'''my_moudule1模块的代码
__all__ = ['testA']

def testA():
    print("testA")

def testB():
    print("test")

'''

'''导入模的代码
from my_module1 import *
    testA()#ok的
    testB()#报错


'''