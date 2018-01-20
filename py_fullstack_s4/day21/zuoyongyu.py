# x=1
# def foo():
#     #x=1000
#     print(x)
#
# foo()
# print(x)
#先找局部名称空间,再找全局名称空间

#先定义后使用!!:
# def bar():
#     print('bar..')
def foo():
    print('from foo')
    bar()

def bar():
    print('from bar')
foo()