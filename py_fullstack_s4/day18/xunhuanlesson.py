# for i in seq:
#     pass
#
# print("ok")

#两个问题：
#　循环次数由序列的一级元素的个数的决定

for item in ["hello",123,[2,3,4]]:
    if item==123:
        continue #结束本次循环
        #break    #结束整个循环
#     print("ok")
    print(item)
else:
    print("ending for")

print("ending")
# print(range(10))
#
# for i in range(10):
#     print("ok")



#while 条件表达式：
#执行代码
# while 2>1:
#     print("ok")

i=1
while i<101:
    print(i)
    i+=1

for i in range(1,101):  #等价于
    print(i)


#遍历并且打印索引方法一：
# count=0
# for i in [11,22,33]:
#     print("%s----$s"%(count,i))
#
#     count+=1

#方法二
# l=[1,2,333,4]
# for i in l:
#     print(l.index(i),i)

#方法三：
l=[1,2,333,4]
for i,v in enumerate(l):
    print(i,v)


#遍历并且打印索引方法一：
# count=0
# for i in [11,22,33]:
#     print("%s----$s"%(count,i))
#
#     count+=1

#方法二
# l=[1,2,333,4]
# for i in l:
#     print(l.index(i),i)

#方法三：
l=[1,2,333,4]
for i,v in enumerate(l):
    print(i,v)


