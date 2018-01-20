#内建函数
print(sum)

#自定义函数
'''
#############
alex SB SB
#############
'''
def print_line():
    print('#'*13)

def print_msg():
    print('alex SB SB')

print_line()
print_msg()
print_line()

'''

def 函数名(arg1,arg2,arg3):
    '描述信息'
    函数体
    return 1

'''

#先定义，后使用

def foo():
    'foo function'
    print('from the foo')
#print(foo._doc_)


def bar(x,y):
    print('from bar')
    res=x+y
    return res #运行没有结果，因为:无参函数不需要有返回值


#无参函数:
# def tell_cmd():
#     msg='''
#     1 查看
#     2 购买
#     '''
#     print(msg)

#有参函数

def bar(x,y):
    print(x)
    print(y)

def auth():
    pass

def list_goods():
    'shoppinglist'
    pass

def buy():
    'buy something'
    pass


def interactive():
    'user interactive'
    list_goods()
    money=input(">> ")
    goods=input(">> ")
    buy(money,goods)

#函数的调用
foo()
bar(1,2)

res=bar(1,2)
res1=bar(1,2)*10
print(res1)

res2=bar(bar(1,2),3)

print(res2)



