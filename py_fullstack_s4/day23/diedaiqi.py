# l=['a','b','c','d','e']
# i=0
# while i < len(l):
#     print(l[i])
#     i+=1

# for i in range(len(l)):
#     print(l[i])
# print('==============================================')
# #迭代器
# #可迭代的:本身有d.__iter__()方法,
# d={'a':1,'b':2,'c':3}
# d.__iter__() #iter(d)
# i=d.__iter__()
# print(i.__next__())
# print(i.__next__())
# print(i.__next__())
# print(i.__next__())

# d={'a':1,'b':2,'c':3}
# i=iter(d)
# while True:
#     try:
#         print(next(i))
#     except StopIteration:
#         break
#
# l=['a','b','c','d','e']
# i=l.__iter__()
# while True:
#     try:
#         print(next(i))
#     except StopIteration:
#         break


# d={'a':1,'b':2,'c':3}
# for k in d: #d.__iter__()
#     print(k)
#
#
# s={1,2,3,4}
# for i in s:
#     print(i)
#
# with open('a.txt','r') as f:
#     for line in f:
#         print(line)
#
# f=open('a.txt','r')
# f.__next__
# f.__iter__
# print(f)
# print(f.__iter__())

# for line in f: #f.__iter__()
#     print(line)

l=[1,2,3]
i=iter(l)
print(next(i))
print(next(i))
print(next(i))

for x in i:
    print(x)


for x in i:
    print(x)

for x in i:
    print(x)
        #why use iteration:
  #   优点
  # 1.迭代器提供一种不依赖索引的取值方式，可以遍历没有索引的可迭代对象（字典，集合）
  # 2.迭代器与列表相比，迭代器是惰性计算的，更省内存
  #
  #   #缺点：
  #   1.迭代器无法获取长度,不如列表索引取值方便
  # 　2.一次性，只能往后取值

#查看可迭代对象与迭代器对象
from collections import Iterable,Iterator

s='hello'
l=[1,2,3]
t=(1,2,3)
d={'a':1}
set1={1,2,3,4}
f=open('a.txt')

#是否　可迭代对象
s.__iter__()
l.__iter__()
t.__iter__()
d.__iter__()
set1.__iter__()
f.__iter__()
print(isinstance(s,Iterable))
print(isinstance(l,Iterable))
print(isinstance(t,Iterable))
print(isinstance(d,Iterable))
print(isinstance(set1,Iterable))
print(isinstance(f,Iterable))

#是否　迭代器:
print(isinstance(s,Iterator))
print(isinstance(l,Iterator))
print(isinstance(t,Iterator))
print(isinstance(d,Iterator))
print(isinstance(set1,Iterator))
print(isinstance(f,Iterator)) #迭代器