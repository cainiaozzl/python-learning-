def auth2(auth_type):
    def auth(func):
        def wrapper(*args,**kwargs):
            if auth_type == 'file':
                name=input('username: ')
                password=input('password: ')
                if name == 'zhejiangF4' and password == 'sb945':
                    print('auth successful')
                    res=func(*args,**kwargs)
                    return res
                else:
                    print('auth error')
            elif auth_type == 'sql':
                print('TM不懂')
        return wrapper
    return auth
@auth2(auth_type='sql')
def index():
    print('welcome to index page')

index()


