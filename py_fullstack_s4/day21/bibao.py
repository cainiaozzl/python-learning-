#x=1000000000000
# def f1():
#     x=1
#     def f2():...
#     return f2
# f=f1()
# print(f)

# def f1():
#     x=1
#     def f2():
#         print(x)
#     return f2
# f=f1()
# print(f)
# f()

#闭包:首先必须是内部定义的函数,该函数包含对外部作用域,而非全局作用域名字的引用
# x=1
# def f1():
#     x=1000
#     #y=1
#     def f2():
#         print(x)
#     return f2
#
# f=f1()
# f()
# print(f.__closure__)
# print(f.__closure__[0].cell_contents)
# print(f.__closure__[1].cell_contents)

# from urllib.request import urlopen
# def get(url):
#     return urlopen(url).read()
#
# print(get('http://www.baidu.com'))

from urllib.request import urlopen
def f1(url):
    def f2():
        print(urlopen(url).read())

    return f2

python=f1('http://www.python.org')

#下载页面+'http://www.python.org'

python()
python

