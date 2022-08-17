#求三数之和：
def sum_num(a,b,c) :
    return a+b+c

a,b,c=map(int,input().split())
result = sum_num(a,b,c)
print(result)


#求3数平均值：
a,b,c=map(int,input().split())
def sum_num(a,b,c) :
    return a+b+c

def average_num(a,b,c) :
    sum_result=sum_num(a,b,c)#嵌套了啊，注意注意!
    return sum_result/3#注意这里除法计算结果会是浮点数数形式
result=average_num(a,b,c)
print(result)