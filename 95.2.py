
def f(*q,**p):#双*放后面
    for i in p.items():
        print(i)
    for j in q:
        print(j)
f(2,3,i=7,o=8)
#先填充*q，后填充p