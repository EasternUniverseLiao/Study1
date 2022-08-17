#方法1推荐
i=1
result=0
while i<=100 :
    if i%2==0 :
        result+=i
    else:
        result=result
    i+=1
print(result)

#方法2
i=2
result=0
while i<=100:
    result+=i
    i+=2
print(result)