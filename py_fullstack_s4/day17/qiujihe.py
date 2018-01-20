linux = {"alex","jack","rain","zengzilin","sb",'zengzilin'}
python = {"sb","zengzilin","alex","dd","bb"}

print(type(linux))
# #交集：
# print(linux.intersection(python))
# print(linux & python)
#
# #差集：
# print(linux.difference(python)) #打印linux的差集
# print(python.difference(linux)) #打印python的差集
#
# #并集,联合
# print(linux.union(python))
# print(linux | python)
# #对称差集
# print(linux.symmetric_difference(python))
# print(linux ^ python)
#
# linux.update(python) #把python合并到ｌｉｎｕｘ集合中
#
print(linux)
linux.add ("ALEX")
#linux.difference_update (python) #差集并pass给ｌｉｎｕｘ集合，一般不这样用
linux.discard('alex') #删除,如果元素不存在不报错
linux.pop() #随机删除
linux.remove('sb') #删除，如元素不存在会报错
print(linux)

#print(linux.issubset)

