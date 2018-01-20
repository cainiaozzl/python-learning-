def init(func):
    def wrapper(*args,**kwargs):
        res=func(*args,**kwargs)
        next(res)
        return res
    return wrapper

@init
def eater(name):
    print('%s start to eat' % name)
    food_list=[]
    while True:
        food = yield food_list
        print('%s eat %s' %(name,food))
        food_list.append(food)

e = eater('zhejiangF4')
next(e)
print(e.send('123'))
print(e.send('123'))

