


#读操作：
#f=open("test") #在windowa系统可以声明编码f=open("test",encoding="utf8"),或者以GBK形式保存

#读取内容
#data=f.read()
# data=f.read() #data=f.readline(５)读取前五个字符,py3按字符读取，py2按字节读取,所以读取汉字会乱码，
# data2=f.read() #从光标位置 读指定个数的字符

#读取一行
#data=f.readline()
#data2=f.readline()

# data=f.readlines() #读取一个列表结果
# print(data)   #文件默认以utf-8保存，linux默认编码是utf-8所以没有报错，但在windows中文系统是ＧＢＫ,解码会报错
#print("data2",data2)#从打印的光标后


#f.close()

#练习:在第四行末尾加上“岳飞”

count=0

# for line in f.readlines(): ＃这种读法吃掉内存
#     if count==3:
#         line="".join([line.strip(),"岳飞"])
#
#     print(line.strip())
#     count+=1

#方法二：

# for line in f:　#这个读取方法可以优化内存
#     if count==3:
#         line="".join([line.strip(),"岳飞"])
#
#     print(line.strip())
#     count+=1

#写操作:
# f=open("test",mode="w")
# f=open("test2",mode="w")
# f=open("test3",mode="w",encoding="utf8") #指定编码格式
# f=open("test3",mode="a",encoding="utf8")#在光标最后位置后面追加
# f=open("test4",mode="w")
# f=open("test4",mode="x") #新建一个文件，已存在会报错，防止覆盖原来的文件
#f.write("dd")　文件对象,默认只读，需指定可写模式

#f.write("hello\nworld") #覆盖原来的，或者不存在便会新建

#print(f.readlines()) #指定了w,就不可读了

# f.write("hello test4")

#f.close() #这个close方法不写,程序也会关闭，因为程序会写进缓存,内存，之后再一次性写入磁盘

#f.flush() #不用写如缓存等待，直接写入磁盘

# import time
# time.sleep(100)

#进度条:

# import sys

#sys.stdout.write("hello") #输出终端屏幕

# for i in range(100):
#     s="\r%d%% %s"%(i,"#"*i)
#     sys.stdout.write("#") #终端就是一个缓存文件
#     sys.stdout.flush()
#
#     import time
#     time.sleep(0.5)
#
# f.close()

#给上述打印输出加上进度条百分比

#可读可写模式 r+ w+ a+

#r+
# f=open("test5",mode="r+") #读写模式
# print(f.read())
# f.write("where is xialv?") #追加的形式改写文件
#print(f.read())

#w+

# f=open("test5","w+")
# f.write("hello林海峰")
# print(f.read()) #不能在屏幕读出，因为内容在文末尾光标之后
#f.seek(0) #讲光标定位在开始的位置,便可输出屏幕
#f.seek(5) #将光标移动到第五个字节,不同于read方法,他是按字节移动的
# f.seek(1,2)#一定要按字节模式操作（rb）
#f.seek(-3,2)


# print(f.tell()) #指出光标所在的字节位置
# print(f.read())
 #

#a+ 总是在最后的位置添加内容
# f=open("test5","a+")
# f.seek(0)
# print(f.read())
#
# f.seek(0)
# f.write("alex")

#总结：
#r w a w:覆盖写,　a:追加写
#w+:覆盖写，想读取内容:seek调整
#a+:光标默认在文件最后位置，不管光标位置,一定是追加写:想读取内容，通过seek调整

#ｓｅｅｋ的应用,比如断点续传

#rb   wb   ab :以字节模式进行处理

#f=open("test5","r")
# f=open("test5","rb") #直接以字节显示
# print(f.read())

# f=open("test6","wb")
#
# f.write("hello李杰".encode("utf8")) #需要指定编码
#
# f.close()
#
# f=open("test6","ab")

with open("test6") as f: #==> f=open("test6")
    f.read() #推荐用此方法打开；修改文件