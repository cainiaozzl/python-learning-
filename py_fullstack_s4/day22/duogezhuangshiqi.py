import time
current_login={'name':None,'login':False}
def timmer(func):
    def wrapper():
        #print(func)
        start_time=time.time()
        func() #执行最原始的index
        stop_time=time.time()
        print('run time is %s' %(stop_time-start_time))
    return wrapper
def auth2(auth_type='file'):
    def auth(func):
        def wrapper(*args,**kwargs):
            if current_login['name'] and current_login['login']:
                res=func(*args,**kwargs)
                return res
            if auth_type == 'file':
                name=input('username: ')
                password=input('password: ')
                if name == 'zhejiangF4' and password == 'sb945':
                    print('auth successful')
                    res=func(*args,**kwargs)
                    current_login['name']=name
                    current_login['login']=True
                    return res
                else:
                    print('auth error')
            elif auth_type == 'sql':
                print('TM不懂')
        return wrapper
    return auth

@timmer
@auth2(auth_type='file')
def index():
    print('welcome to index page')


@auth2()
def home():
    print('welcome to home page')

index()
home()