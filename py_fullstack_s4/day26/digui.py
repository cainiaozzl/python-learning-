# import time
# def age(n):
#     print('---->',n)
#     time.sleep(1)
#     if n == 1:
#         return 10
#     else:
#         return age(n-1)+2
#
# print(age(5))
#
# def func(n):
#     if n == 10:
#         return
#     print('from func')
#     func(n-1)
#
# func(10)
'''
1.必须有一个明确的结束条件

2.进入层递归时，问题规模相比上次递归都应有所减少

3.效率不高，递归层次过多，会导致栈溢出
函数调用是通过栈(stack)这种数据结构，没调用一次，栈帧会
'''

data = [1,3,6,7,9,12,14,16,17,18,20,21,22,23,30,32,33,35]
# num=19
# i=0
# while True:
#     if num == data[i]:
#         print('find it')
#         break
#     i+=1

# data=[]
# for i in range(100000):
#     data.append(i)

def search(num,data):
    print(data)
    if len(data) > 1:
        mid_index=int(len(data)/2)
        mid_value=data[mid_index]
        if num > mid_value:
            #num在列表的右边
            data=data[mid_index:]
            search(num,data)
        elif num < mid_value:
            #num在列表的左边
            data=data[:mid_index]
            search(num,data)
        else:
            print('find it')
            return
    else:
        print(data)

search(19,data)


