#名称空间与作用域
 #内置名称空间,全局名称空间,局部名称空间


#全局作用域:内置名称空间,全局名称空间
#局部作用域：局部名称空间
#函数嵌套与嵌套作用域


#函数对象
# def f3():
#     x=1
#     def f4():
#         print(x)
#
#     return f4
#
# x=1000
# f4=f3()
# f4()
#
# def foo():
#     f=f3()
#     x=10000
#     f()
#
# foo()

#闭包:内部函数包含对外部作用域而不是对全局作用域的名字的引用
from urllib.request import urlopen
def get(url):
    def index():
        return urlopen(url).read()
    return index

f=get('http://www.python.org')
print(f.__closure__)
print(f.__closure__[0].cell_contents)

print(f())