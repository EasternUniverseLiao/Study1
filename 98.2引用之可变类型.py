#列表
aa = [10, 20]
bb = aa
print(bb)
print(id(aa))
print(id(bb))#与id(aa)一样

aa.append(30)
print(aa)
print(bb)#列表是可变类型，bb会同步变化，aa修改是改内存中的原数据，bb也会跟着一起修改
print(id(aa))#与修改前的id一样
print(id(bb))#与id(aa)一样
