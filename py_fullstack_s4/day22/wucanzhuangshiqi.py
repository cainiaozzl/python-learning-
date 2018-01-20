#为什么用装饰器以及开放封闭原则

#什么是装饰器
#import time
# def timmer(func):
#     def wrapper(*args,**kwargs):
#         start=time.time()
#         res=func(*args,**kwargs)
#         stop=time.time()
#         print('run time is %s' %(stop-start))
#     return wrapper




# @timmer #index=timmer(index)
# def index():
#     time.sleep(3)
#     print('welcom to oldboy')
#
# index()

import time
# def timmer():
#     pass

def timmer(func):
    def wrapper():
        #print(func)
        start_time=time.time()
        func() #执行最原始的index
        stop_time=time.time()
        print('run time is %s' %(stop_time-start_time))
    return wrapper

@timmer #index=timmer(index)
def index():
    time.sleep(1)
    print('welcom to oldboy')

index() #--=--->wrapper()

@timmer
def home():
    time.sleep(2)
    print('welcome to home page')

# def my_max(x,y):
#     print('from my_max func')
#     return x+y

home()
