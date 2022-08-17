'''
zip([可迭代对象])，返回一个元组



'''
#zip()打包
a = [1,2,3]
print(zip(a))#<zip object at 0x014EE488>返回的是地址
# print(*zip(a))
print(list(zip(a)))#[(1,), (2,), (3,)]用list
print(tuple(zip(a)))#((1,), (2,), (3,))用tuple

b = ['q','w','e']
print(list(zip(a,b)))#[(1, 'q'), (2, 'w'), (3, 'e')]

c = ['q','w']
print(list(zip(a,c)))#[(1, 'q'), (2, 'w')]

#zip(*...)反打包
zipped = zip(a)
print(list(zip(*zipped)))

#zip与for结合
for i in zip(a):
    print(i)