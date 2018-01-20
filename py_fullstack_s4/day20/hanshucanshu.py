# def auth():
#     name = input('username:')
#     pwd = input('password:')
#     if name == 'egon' and pwd == '123':
#         print('login successful')
#     else:
#         print('login error')
#
# auth()
# auth()

def my_max(x,y):
    '''x-->int,y-->int,res=int,calculate max value'''
    res=x if x > y else y
    return res

# print(my_max(1,2))
# print(my_max('a','b'))
# print(my_max('a',1))

# def my_min(x:int,y:int)->int: #无意义,建议用函数描述
#     print(x if x < y else y)
#
# my_min(1,2)
# my_min('a','b')
# print(my_min.__annotations__)

#函数的参数介绍

x=100000 #不受内部的影响
# def foo(x,y): #在函数定义阶段，括号内定义的参数>>形式参数(实质是变量名)
#     print(x)
#     print(y)
#
# foo(1,2) ##在函数调用阶段,括号内定义的参数>>实际参数(实质是变量值，但也可以是变量) #调用时生效
#==>x=1,y=2
print(x)
#但也可以是变量
# a=100
# b=200
# foo(a,b)

# x=[1,2,3]
# y=1
# foo(x,y)

def bar(x): #x=1
    print(x)
    x=3
# a=1
# bar(a)
# print(a)
x=1#这个跟函数内部的x无关
bar(x)
print(x)


def bar(x): #x=[1,2,3]
    print(x)
    x.append(4)#列表是可变类型，会导致全局的变动,不可取
#函数内的参数类型必须是不可变类型
x=[1,2,3]
bar(x)
print(x)


