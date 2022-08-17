num1=3
str1="6"
print(type(float(num1)))
print(float(num1))#3.0
print(float(str1))#6.0
print(type(str(num1)))

#元组圆括号，列表方括号
list2=[1,2,3]
print(tuple(list2))


#eval就是把字符串转换为原本形式
str2="5"
str3="6.0"
str4="[88,99,99,]"
str5="(00,00,99)"


print(type(eval(str2)))
print(type(eval(str3)))
print(type(eval(str4)))
print(type(eval(str5)))
