#break和continue
#break：终止此循环
#continue：退出当前循环一次继而执行下一次循环代码
'''
举例：一共吃五个苹果，吃完第一个吃第二个
情景一：吃完第三个吃饱了，不需要再吃第四第五个苹果，即循环性终止，用break
情景二：吃到第三个吃出一个大虫子，这个苹果不吃了，从第四个苹果开始吃，用continue
'''
i=1
while i<=5 :
    if i==4 :
        print('吃饱了，不吃了')
        break
    print(f'吃了第{i}个苹果')
    i+=1

i = 1
while i <= 5:
    if i == 3:
        print('有虫，不吃这个')
        #使用了continue一定要在之前修改计数器，否则将进入死循环
        i+=1
        continue
    print(f'吃了第{i}个苹果')
    i += 1

