
# class Garen:
#     camp = 'Demacia'
#     def attack(self):
#         print('attack')


#如何使用类
x=int(10)
print(x)

#一：实例化
# obj=Garen()
# print(obj)

#二:引用类的特征（类的变量）和技能（类的函数）
# print(Garen.camp)
# Garen.attack(111223)

#如何使用实例
class Garen:
    camp='Demacia'
    def __init__(self,nickname): #g1.nick='草丛伦'
        self.nick=nickname
    def attack(self,enemy):
        print('------->',self.nick)
        print('%s attack %s' %(self.nick,enemy) )

g1=Garen('草丛伦') #Garen.__init__(g1,'草丛伦')
g2=Garen('猥琐伦')


print(g1.nick)
# print(g1.camp)
# print(g1.attack) #bound method 对象g1
# print(Garen.attack)

#Garen.attack() #调用的是函数
#g1.attack()
g1.attack('alex')
#g1.nick() #self=自动传值g1
#g1.attack('alex')
print(g1)


# print(g2.nick)
# print(g2.camp)


#小结
#类:一实例化　二引用名字(类名.变量名,类名.函数名)

#实例:引用名字（实例名.类的变量；实例名.绑定方法；实例名自己的变量性）

class Garen:
    camp='Demacia'
    def __init__(self,nickname): #g1.nick='草丛伦'
        self.nick=nickname
    def attack(self,enemy):
        print('------->',self.nick)
        print('%s attack %s' %(self.nick,enemy) )

print(Garen.camp) #查

#改
Garen.camp='aaaaa'
print(Garen.camp)

#删
# del Garen.camp
# print(Garen.camp)

#增

Garen.x=1
print(Garen.x)

#实例　的改查
g1=Garen('alex')
print(g1.nick)
g1.nick='asb'
print(g1.nick)
#删
del g1.nick
print(g1.nick)
#增
g1.sex='female'
print(g1.sex)
