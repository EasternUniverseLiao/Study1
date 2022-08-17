#需求：八位老师，三个办公室，随机分配
'''
步骤：
1.准备老师，办公室
2.分配老师到办公室
3.检验

'''
import random
teather_list =['a','b','c','d','e','f','g','h']
offics = [[],[],[]]

for name in teather_list :
    num = random.randint(0, 2)
    offics[num].append(name)
print(offics)
#开始验证
a=1
for i in offics :
    print(f'办公室{a}的人数是{len(i)},老师分别是：',)
    for name in i :
        print(name)
    a+=1