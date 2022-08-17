#if嵌套
'''
坐公交:如果有钱可以上车，没钱不能上车;上车后如果有空座，则可以坐下;如果没有空座，就要站着。
'''
money=int(input('有钱请输1，忘带钱请输0:'))


if money==1:

    print(f'土豪,请上车')
    seat = int(input('有座请输1，无座请输0：'))
    if seat==1:#判断是否能坐下
        print(f'有空座，能坐下')
    else:
        print(f'没有空座，站着等')
else:
    print(f'朋友，没带钱就跟着跑，跑快点')