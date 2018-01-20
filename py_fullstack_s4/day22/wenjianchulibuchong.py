# current_login={'name':None,'login':False}
#
# with open('user.db','w') as f:
#     f.write(str(current_login))

with open('user.db','r') as f:
    x=f.read()
    print(x,type(x))

print(eval(x)['login'])