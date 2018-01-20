name = "Alex Li；Rain Wang;Jack"
name.strip() #脱
print(name.strip())

print(name.split(";")) #分割，把一个字符　按空格分割成列表

print(len(name)) #长度
name1 = "suhaozhi,qinzhen,lizhi"
print(name1.index("h"))
print(name1[0:8]) #切片
print(name1[9:16])
name2 = ["0", "1", "2", "3", "4", "5", "6", "7", "8" ]
print("-->",name1[-1:-6]) #从左往右3
print("-->",name1[-6:-1]) #顾头不顾尾
print("-->",name1[-6:]) #切到最后
print("-->",name1[0::2]) #２步长
print(name2[0::2])
