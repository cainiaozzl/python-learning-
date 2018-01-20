#创建形式　可迭代对象：能够进行for循环
l=[1,"hello",[4,5],{"name":"egon"}]
l2=list([1,23,3])
l3=[1,43,["hello",334],3,77]
print(l2)
print(type(l2))

#查：切片[:]
# print(l3[-2:])
#
# l3.append("yuan") #只能加一个
# print(l3)
#
# l3.extend([7,8])
# print(l3)
#
# #删除
# l3.pop(1)
# print(l3)
#
# l3.remove(1)
# print(l3)
#
#
# del l3[2]
# print(l3)

#改　赋值操作

print(id(l3))

l3[2][0]="yuan"
print(l3)

# l3.insert(3,"fgg")
#print(l3)


l4=[12,3]
l4.clear()
print(l4)

l4=[] #直接赋空值，效率比ｃｌｅａｒ高

[4,35,554,65,4].count(4) #计算元素的个数


print(len(l3))

# l5=["A","a","B"]
# l5.sort()
# print(l5)

l5=["A","a","B"]
l5.sort(reverse=True) #反向排序
print(l5)
print(sorted(l5))

[1,2,4,553,53].reverse()

