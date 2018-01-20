import time
def timmer(func):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        func(*args,**kwargs) #home(name)
        stop_time=time.time()
        print('run time is %s' %(stop_time-start_time))
    return wrapper


@timmer
def home(name):
    time.sleep(2)
    print('welcome to %s home page' %name)

home('dragon')

@timmer
def auth(name,password):
    print(name,password)
auth('egon','123')

@timmer
def tell():
    print('=============-------')
home('dragon') #wrapper('dragon')
auth('egon','123') #wrapper('egon','123')
tell()