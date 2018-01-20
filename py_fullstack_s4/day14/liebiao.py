#names = [ ]
names = ["苏浩至","秦臻","李志","炎龙","饱满","骗子","李志"]
print(names)
#改
names[names.index("骗子")] ="徐雨轩"
print(names[-1])
print(names.index("李志")) #返回元素的索引\下标
print(names[3:5])
print(names.count("李志")) #统计
#print(type(names))

names.append("光头") #追加
print(names)

#插入
names.insert(4,"陈涛")
names.insert(3,"洪志强")
print(names)

#删除
print(names.pop(4)) #删除，默认删除最后－个
#print(names)
names.remove("李志")
del names[1]

print(names)