# n = int(input())  # n为待转换的十进制数
# x = int(input())  # x为进制
# # 在这里先考虑2~16进制内
# a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
# b = []
# while True:
#     t = n % x
#     n //= x
#     b.append(a[t])
#     if n == 0:
#         break
# for i in range(len(b) - 1, -1, -1):
#     print(b[i], end='')
# # 　类比２进制的算法
# # for i in b[::-1]:
# #     print(i,end='')



# 任意进制转换
import functools
# 自定义生成5进制转2进制
def num5to2_list(numMtoN_list,m=5,n=2):
    return functools.partial(numMtoN_list,m=5,n=2)
data = '114'
res = num5to2_list(data,5,2)

>>> data = [1,1,4]
>>> res = numMtoN_list(data,5,2)
# res = num5to2_list(data,5,2) # 效果相同
res = [1, 0, 0, 0, 1, 0]


print(res)
