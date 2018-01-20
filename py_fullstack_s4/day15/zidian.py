'''
#names = [
    ["qinzhen",'28','大保健','河北沧州'],
    ['qinzhen2','28','大保健','河北沧州']
]
'''

#key:value 键：值对
#字典是无序的
names = {
    37148119950532:{"name":"Alex Li","age":22},
    110232323:{"name":"Jack Li","age":52},
    111:["rain1"],
    222:["rain2"],
    333:["rain3"],
    118: ["rain from name1"],
}

dict2 = {
    118: ["rain"],
    113:["rain"],
}

print(names[37148119950532]["name"])

names.update(dict2)
print(names)


 #改
names[111][0] = "QinZhen"
names[111].append(28)
names[222] = "mike"
print(names)


#增


 #删

 #print(names.pop(111))
print(names.pop(1100,None)) #如果删除的值不存在可以附一个空的值

print(names.popitem()) #随机删除

#del names[112]
print(names)
#
#查
print(names)
print(names.get(113)) #没有值会返回none

print(113 in names) #判断是否在字典里有这个key

#loop 循环

for i in names:
    print(i,names[i])

#for i in names
#print(i) 只打印key

for i in names:
    print(i,names[i])

 #for k,v in names.items():  #不要用,效率低
  #   print(k,v)

print(names.keys()) #只打印键
print(names.values()) #只打印值


