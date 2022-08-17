def return_num():
    return 1
    return 2#此时在return后边的代码是不执行的
result = return_num()
print(result)


#函数多返回值

def return_num2():
    return 1,2#reutrn可以返回元组，列表，字典
result2 = return_num2()
print(result2)#(1, 2)返回的是元组