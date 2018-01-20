#嵌套调用:
def my_max(x,y):
    res=x if x > y else y
    return res

print(my_max(10,100))

def my_max4(a,b,c,d):
    res1=my_max(a,b)
    res2=my_max(res1,c)
    res3=my_max(res2,d)
    return res3
print(my_max4(1,20,3,4))

# def tell_cmd():
#     pass
# def search():
#     pass
#
# def main():
#     tell_cmd()
#     choice=input('>>')
#     if choice == '1':
#         search()
#
# main()


#嵌套定义:
x=1111111111111111111111
def f1():
    x=1
    print('-------->f1',x)
    def f2():
        #x=2 #先找局部名称空间,没有再找外层的全局名称空间
        print('---->f2',x)
        def f3():
            #x=3  #先找局部名称空间,再找全局名称空间
            print('-->f3',x)
        f3()
    f2()

f1()