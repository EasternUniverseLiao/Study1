#语法
try:
    '可能发生错误的代码'
except:
    '如果出现异常执行的代码'

#案例
try:
    f = open('tset3.txt', 'r')
except:
    f = open('tset3.txt', 'w')
