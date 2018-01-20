import time
def timmer(func):
    def wrapper(*args,**kwargs):
        start_time=time.time()
#res=func 接受返回值，并且存储:
        res=func(*args,**kwargs) #my_max(1,2)
        stop_time=time.time()
        print('run time is %s' %(stop_time-start_time))
        return res
    return wrapper

@timmer
def my_max(x,y):
    print('my_max function')
    res=x if x > y else y
    return res

res=my_max(1,2) #res=wrapper(1,2)
print('=====>',res)