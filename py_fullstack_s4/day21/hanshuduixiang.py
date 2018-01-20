# def foo():
#     print('foo')

#print(foo)

#函数可以被赋值
# f=foo
# print(f)
# f()

# #把函数当成参数传递
# def bar(func):
#     print(func)
#     func()
#
# bar(foo)

#把函数当成返回值
# def bar(func):
#     print(func)
#     return func
#
# f=bar(foo)
# print(f)
# f()

x=1
print([1,x,3,4,])

def search():
    print('search')

def add():
    print('add')

def delete():
    print('delete')

def change():
    print('change')

def create():
    print('create')

def tell_msg():
    msg='''
    search:查询
    add:添加
    delete:删除
    change:改变
    create:新建
    '''
    print(msg)

cmd_dic={
    'search':search,
    'add':add,
    'delete':delete,
    'change':change,
    'create':create
}


while True:
    tell_msg()
    choice=input('please input your choice:').strip()
    #print(cmd_dic[choice])
    cmd_dic[choice]()