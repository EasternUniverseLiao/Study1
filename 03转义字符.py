#转义字符
#\n换行
#\t制表符(四个字母距离）
#\r加空行



print('hello')
print("world")
print("hello\nworld")
print("abcd")
print("\tabcd")
print("llll")
print('-----------')

# \b退格
# \f换页
# \r回车
# \n换行
# \t水平制表符
# \v垂直制表符
# \ooo三位八进制数对应的字符
#
print('\\ooo')

# \xhh两位十六进制对应的字符
#
# \uhhhh四位十六进制表示的Unicode字符



path = "pacacdav\nfadna"
print(path)# 会换行输出
# 用r'不对字符串内部操作
path = r"pacacdav\nfadna"
print(path)