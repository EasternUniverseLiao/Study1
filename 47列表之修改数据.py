#修改指定下标数据
list1=['Tom','Lily','Rose']
list1[0] = 'xiaoming'
print(list1)


#逆置.reverse()
list2=[1, 5, 2, 3, 6, 8]
list2.reverse()#不能与下一步复合
print(list2)



#排序:sort()
#语法：列表序列.sort(key=None,reverse=False)
#注：reverse表示排列顺序，reverse=True 降序，reverse=False 升序 （默认）


list3=[1,5,3,3,6,7,8]
list3.sort()#默认升序
print(list3)
list3.sort(key=None,reverse=True)#用False为升序
print(list3)


#注意：列表可变类型，一旦出现：列表a=列表b，对哪个列表修改都会改变另一个，所以要有复制这个操作，看下一章48列表之复制数据