f=open('a.txt','w')
#f.readline()
#f.write('111111111\n')
#f.write('ddddddddd\n')
#f.writelines(['11111\n','22222\n']) #等价于以上两行

f.write('111111111\n')
f.write('111111111\n')
f.write('111111111\n')
f.write('111111111\n')
f.write('111111111\n')
f.write('111111111\n')
f.write('111111111\n')
f.write('111111111\n')
f.seek(0) #光标移动到行首
f.truncate(3) #在ｗ模式下，保留三个字符，其余都清空
f.close()

with open('a.txt') as f,open('b.txt') as f2:
    pass