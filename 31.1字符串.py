# input接收数据类型是字符串
print('''I am Tom''')  # 三引号也可以书写字符串，
print('''I
am Tom''')  # 并支持回车换行
print('''I 'm Tom''')
a = 'hello' \
    ' world' \
    '!'
print(a)
b = 'I\'m TOM'
print(b)

# 补充特殊字符串可以表示无穷大
a = float("inf")
print(a > 10000000000)
a = float("-inf")
print(a < 10000000000)
