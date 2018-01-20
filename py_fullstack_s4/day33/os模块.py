import os

# print(os.getcwd())
#
# f=open("test.txt","w")
#
# os.chdir("/home/zzl/PycharmProjects/py_fullstack_s4/day32") # cd
# #
# f=open("test2.txt","w")
# #
# print(os.getcwd())


# os.makedirs("aaaaa/bbb")
#os.removedirs("aaaaa/bbb")

#print(os.listdir("/home/zzl/PycharmProjects/py_fullstack_s4/day33"))

# print(os.stat(r"C:\Users\Administrator\PycharmProjects\py_fullstack_s4\day33\test.txt"))
print(os.stat(r"/home/zzl/PycharmProjects/py_fullstack_s4/day33/test.txt"))
#
#
# '''
# os.stat_result(st_mode=33206, st_ino=10133099161702379, st_dev=3233102476, st_nlink=1, st_uid=0, st_gid=0, st_size=0, st_atime=1493176560, st_mtime=1493176614, st_ctime=1493176560)
#
# '''

# "yuan"+os.sep+"image"

# print(os.name)
# print(os.system("dir"))

abs=os.path.abspath("test.txt")
print(os.path.basename(abs))
print(os.path.dirname(abs))

#路径拼接
s1="/home/zzl/PycharmProjects"
#
s2="py_fullstack_s4/day33"
#
#print(s1+os.sep+s2)
#
ret=os.path.join(s1,s2)   # 推荐方式
print(ret)



