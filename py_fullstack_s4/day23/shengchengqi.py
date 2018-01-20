#生成器与return区别?
     #return只能返回一次值，函数就彻底结束；而yield能返回多次值
#yield的作用：
    #yield把函数变成生成器-->迭代器
    #函数在暂停以及继续下一次运行时的状态由yeild保存
from collections import Iterator
#生成器就是一个函数，这个函数包含yield关键字
def test():
    print('first')
    yield 1 #return 1
    print('second')
    yield 2
    print('third')
    yield 3
    print('fourth')
    yield 4
    print('fifth')
    yield 5


g=test()
# print(g)

# print(isinstance(g,Iterator))

res=next(g)
print(res)

res=next(g)
print(res)



def countdown(n):
    print('start coutdown')
    while n > 0:
        yield n
        n-=1
    print('done')

g=countdown(5)

# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

#捕获异常
# for i in g:
#     print(i)
#
# while True:
#     try:
#         print(next(g))
#     except StopIteration:
#         break

#迭代获取无穷个值
def func():
    n=0
    while True:
        yield n
        n+=1

f=func()
print(next(f))

import time
def tail(file_path):
    with open(file_path,'r') as f:
        f.seek(0,2)
        while True:
            line=f.readline()
            if not line:
                continue
            else:
                print(line)
tail()




