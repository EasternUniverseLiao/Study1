# last=0
# this=1
# n=int(input())
# i=1
# while i<n :
#     copy_last=last
#     last=this
#     this+=copy_last
#     i+=1
# print(this)
a = 0
b = 1
n = int(input())
i = 1
while i<= n:
    a,b = b,a+b
    i+=1
print(a)
