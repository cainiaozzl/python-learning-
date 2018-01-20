# #继承Thread式创建
#
# import threading
# import time
#
# class MyThread(threading.Thread):
#
#     def __init__(self,num):
#         threading.Thread.__init__(self)
#         self.num=num
#
#     def run(self):
#         print("running on number:%s" %self.num)
#         time.sleep(3)
#
# t1=MyThread(56)
# t2=MyThread(78)
#
# t1.start()
# t2.start()
# print("ending")
import time
class Card:
    bank="工行"
    def __init__(self,card_number,own_name,money,card_date):
        self.card_number=card_number
        self.own_name=own_name
        self.money=money
        self.card_date=card_date
    def view(self):
        print("账户信息,%s欢迎登录"%(self.bank),self.card_number,self.own_name,self.money,self.card_date)
    def take(self,take_money):
        mum=self.money-take_money
        print("你一共取了%s，余额为%s",take_money,mum)

c1=Card("6220144549585","lzh",10000,time.asctime())
# print(c1.__dict__)#为什么我们可以用字符串操作类下的数据属性和函数属性，因为它们都是以字典的形式存在
print(hasattr(c1,"bank"))#hasattr,以字符串的形式获取类下的属性名，如果存在返回真
print(getattr(c1,"take"))#getattr,得到类下的一个函数属性，如果存在返回一个绑定的函数方法
print(getattr(c1,"take1","没有这个方法"))#getattr，如果没有指定的属性，则报错，getattr还可以添加一个自定义的报错值
#当添加这个值后，getattr方法会返回这个定义值
setattr(c1,"addr","沙河分行")#该方法添加类的数据属性
setattr(c1,"bank","爱存不存")#此处可以修改类中的数据属性值
print(c1.bank)
print(c1.addr)
delattr(c1,"bank")
print(c1.__dict__)
#简单的应用示例,我们可以通过用户输入字符串的形式确定类这个对象中是否有这个操作，
# 如果有，就执行，显示结果，没有就不做任何操作
if hasattr(c1,"view"):
    func=getattr(c1,"view")
    res=func()
    print(res)
else:
    pass



