# def aaa(func):
#     def bbb(*args,**kwargs):
#         res=func(*args,**kwargs)
#         return res
#     return bbb

# def auth(func):
#     def wrapper(*args,**kwargs):
#         #认证功能
#         res=func(*args,**kwargs):
#         return res
#     return wrapper
#
# def timmer(func):
#     def wrapper(*args,**kwargs):
#         res=func(*args,**kwargs)
#         return res
#     return wrapper
#
# def auth2(x,y):
#     def auth(func):
#         def wrapper(*args, **kwargs):
#             # 认证功能
#             res = func(*args, **kwargs):
#             return res
#
#         return wrapper
#     return auth
# @auth2(x=1,y=2)
# def index():
#     print('from index')
#
# index()

import time
from functools import wraps
def timmer(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        '''test'''
        start_time=time.time()
#res=func 接受返回值，并且存储:
        res=func(*args,**kwargs) #my_max(1,2)
        stop_time=time.time()
        print('run time is %s' %(stop_time-start_time))
        return res
    return wrapper

@timmer
def func(x):
    '''functest'''
    print(x)

func(1)
print(func.__doc__)
