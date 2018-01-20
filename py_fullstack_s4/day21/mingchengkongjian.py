import time
class Foo:
    pass

x=1 #局部名称空间
def funcname(): #局部名称空间
    y=100
    print(y)

print(x)
funcname()
#print(y) NameError: name 'y' is not defined
#内置名称空间
#全局名称空间
#局部名称空间
def func2():
    print(y)
