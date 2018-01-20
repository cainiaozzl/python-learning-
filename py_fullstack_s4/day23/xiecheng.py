def eater(name):
    print('%s start to eat food' %name)
    food_list=[]
    while True:
        food=yield food_list
        print('%s get %s ,to start eat' %(name,food))
        food_list.append(food)

    print('done')

e=eater('刚但')
print(next(e))
print(e.send('包子'))
print(e.send('韭菜包子'))
print(e.send('大蒜包子'))
#print(e.send('辣条包子'))
#print(e.send('榴莲包子'))
