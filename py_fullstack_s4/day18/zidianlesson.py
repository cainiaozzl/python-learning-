
#python中唯一具有映射关系的数据类型：字典的查询效率高于列表
print(bool(-1))
d={1:"yuan","name":"alex"}

#查
print(d["name"])

v=d.get("names",None) #推荐
print(v)

if not v:
    pass
#遍历
for i in d:
    #print(i,"---->".d[i])
    print("%s--->%s"%(i,d[i]))

print(list(d.keys()))
print(d.values())
print(d.items())

#增加
d={1:"yuan","name":"egon"}

#d["age"]=123
#print(d)

#修改
d[1]=666
print(d)

#删除

ret=d.pop(1)
print(ret)
print(d)

#del
#更新
d2={"height":123,"sex":"male","name":"alex"}
d.update(d2)
print(d)