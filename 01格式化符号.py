#准备数据
#格式化符号%s字符串，%d正负整数，%f小数，%o八进制，%x16进制,%c字符
age = 18
name='TOM'
weight=56.8
stu_id=1
print("今年我的年龄是%d岁" %age)
print("我的名字是%s"%name)
print("我的体重是%.2fkg"%weight)   #加.x表示保留x为有效数字，不控制默认6位，print("我的学号是%03d"%stu_id)   #加0x表示取x为、位，不足用0填充
#%10d表示调整宽度10个字节，加负号表示右对齐，如：%-10d
print("我的名字是%s,今年我的年龄是%d岁"%(name,age))
print("我的名字是%s,明年我%d岁"%(name,age+1))