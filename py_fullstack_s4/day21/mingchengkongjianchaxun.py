
x=1
def func():
    print('from func')
    x=2
    print(globals())
    print(locals())

#print(globals())
#func()
#print(locals())
a=globals()
func()
b=locals()
print(a == b)