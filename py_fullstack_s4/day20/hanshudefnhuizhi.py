#函数的返回值可以是任意类型
#没有return--->None
#return 1--->1
#return 1,2,3---->(1,2,3)

#situation1：No return--->None
def foo():
    print('from the foo')

res=foo()
print(res)

#situation2:return 1--->1
def my_max(x,y):
    res=x if x > y else y
    return res

res1=my_max(1,2)
print(res1)

#situation3:return multiple values 1,2,3--->(1,2,3)：

def bar(x,y):
    #return (1,2,3,4,5,6,[1,2],{'a':2},{1,2,3})
    return 1,2,3

res2=bar(1,2)
print(res2)

# a,b,c=bar(1,2) #也可以分别打印三个值
# print(a)
# print(b)
# print(c)


def test(): #函数只会执行一个return,其他无效
    return 1
    print('---------')
    print('---------')
    print('---------')
    print('---------')
    return 2
    return 3

res=test()
print(res)