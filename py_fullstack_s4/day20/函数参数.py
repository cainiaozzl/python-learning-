#函数的参数介绍

# def foo(x,y):
#     print(x)
#     print(y)

#在实参的角度

#第一种:按照位置传值
#foo(1,2)
# foo(2,1)

#第二种:按照关键字传值
# foo(x=1,y=2)
# foo(y=2,x=1)

#第三种:混合使用
# foo(1,y=2)
#keyword argument　must follow positional argument

#foo(y=2,1) #报错一：positional argument在前面

#foo(1,x=1,y=2) #报错二：positional argument有多个

#位置参数:必须传值的参数 position arg
# def foo(x,y):
#     print(x)
#     print(y)

#foo(1) #位置参数必须有值,多一个,少一个都不行
#foo(y=2,x=1)

#默认参数
# def foo(x,y=1):
#     print(x)
#     print(y)

#foo(1)
# foo(1,2)
# foo(y=2,x=2)


# def open(file,mode='r'):
#     pass
#
# open('a.txt')

# def register(name,sex='male'):
#     print(name)
#     print(sex)
#
# register('qinzhen')

#default argument must follow non-default argument
# def register(sex='male',name):#occur erro
#     print(name)
#     print(sex)
#
# register('qinzhen')

# def register(sex='male'):
#     print(name) #在定义阶段不会报错,
#     print(sex)
# register() #调用返回的时候会报错NameError: name 'name' is not defined

x='male'
def register(sex=x): #报错
    print(sex)

x='male'
def register(sex=x): #register--------[sex='male'...]
    print(sex)

x=None  #外面
register()

#不推荐下述方式：
# x=[]
# def register(name,name_list=x):
#     name_list.append(name)
#
# register('ASB')
# register('YSB')
# register('WSB')
# print(x)


#args
def foo(x,*args): #args=(2, 3, 4, 5, 6, 6, 'a', 'b')
    print(x)
    print(args)

foo(1,2,3,4,5,6,6,'a','b')

#args与位置参数和默认参数混用,*args要放到位置好参数后面
#def foo(x,y=1,*args):
def foo(x,*args,y=1):
    print(x)
    print(y)
    print(args)

foo(1,2,3,4,5,6,7,y=1000000)

def my_sum(*nums): #nums=(1,2,3,4,5,6,7)
    res=0
    for i in nums:
        res+=i
    return res

#print(my_sum([1,2,3,4,5]))
print(my_sum(1,2,3,4,5,6,7)) #用*num则不需要手动写成序列


#从形参的角度
def foo(*args): #args=(1,2,3)　#foo(x,y,z)
    print(args)
foo(1,2,3)
#从实参的角度
def bar(x,y,z):
    print(x)
    print(y)
    print(z)
bar(*(1,2,3)) #bar(1,2,3)
#bar(*(1,2,3,4))会报错
#**kwargs

# def foo(x,**kwargs):
#     print(x)
#     print(kwargs)
#
# foo(x=1,y=2,a=3,b=4)
# foo(1,y=1,z=2)

#混着用的位置问题
def foo(x,*args,**kwargs):
    print(x)
    print(args)
    print(kwargs)

foo(1,y=1,z=2)

#从实参的角度：
def foo(x,y,z=1):
    print(x)
    print(y)
    print(z)

# foo(**{'x':1,'y':2,'z':3}) #foo(x=1,y=2,z=2)
# foo(**{'x':1,'y':2})
# foo(**{'a':1,'y':2}) #oo(a=1,y=2)

def auth(name,password,sex='male'):
    print(name)
    print(password)
    print(sex)

def foo(*args,**kwargs): #args=('egon','123') kwargs={}
    print('from foo')
    auth(*args,**kwargs)
#auth(*'egon','123'),**{})-->auth('egon','123')
#foo(1,2,3,4,5,x=1,y=2)报错

#foo('egon','123')
#foo('ASB','123',sex='female')
foo(name='ASB',password='123',sex='female') #需要记住
