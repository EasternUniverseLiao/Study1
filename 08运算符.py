#运算符
"""
算术运算符(+加  -减 *乘 /除 //除取商 %除取余数 **指数 （）小括号)
赋值运算符(=将等号右边的结果赋值给等号左边的变量)
复合赋值运算符
'''
+=       c+=a等价于c=c+a
-=       c-=a等价于c=c-a
*=       c*=a等价于c=c*a
/=       c/=a等价于c=c/a
//=      c//=a等价于c=c//a
%=       c%=a等价于c=c%a
**=      c**=a等价于c=c**a
'''
比较运算符
'''
==是否相等
!=是否不相等
>是否大于
>=是否大于或等于

'''
逻辑运算符
'''
and与（且）#都真为真
or或#一真就真，都假才假
not非
'''
"""
num1,float1,str1=10,0.5,"hello world"#多变量赋值
print(num1)
print(float1)
print(str1)

a=b=10#多变量赋相同的值
print(a)
print(b)

x=10
x*=1+2#先算右边
print(x)

a=1
b=2
c=3
print((a<b)and(b<c))#Ture
print((a>b)and(b<c))#False
print((a>b)or(b<c))#Ture
print(not(a>b))#Ture