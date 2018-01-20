#search path /tmp/test
import os
def init(func):
    def wrapper(*args,**kwargs):
        res=func(*args,**kwargs)
        next(res)
        return res
    return wrapper

@init
def search(target):
    '找绝对路径'
    dir_name=yield   #/tmp/test
    g = os.walk(dir_name)
    for i in g:
        for j in i[-1]:
            file_path = '%s/%s' %(i[0],j)
            target.send(file_path)
#打开文件
@init
def opener(target):
    '打开文件，获取文件句柄'
    while True:
        file_path=yield
        with open(file_path) as f:
            target.send((file_path,f))

#读文件


@init
def cat(target):
    while True:
        file_path,f=yield
        for line in f:
            target.send((file_path,line))

@init
def grep(pattern,target):
    '过滤搜索内容'
    while True:
        file_path,line=yield
        if pattern in line:
            target.send(file_path)

@init
def printer():
    '打印文件'
    while True:
        file_path=yield
        print(file_path)


g=search(opener(cat(grep('python',printer()))))
g.send('/tmp/test')

#面向过程的编程思想:流水线式的编程思想,在设计程序时，需要吧整个流程设计出来
    #优点：
    #1:体系结构更加清晰
   #2:简化程序复杂度

  #缺点:
    #1:可扩展性非常差，面向过程用于不经常变的场景：如操作系统,