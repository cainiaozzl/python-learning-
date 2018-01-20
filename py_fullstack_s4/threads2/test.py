
# class A:
#     def __fa(self):
#         print('from A')
#     def test(self):
#         self.__fa() #_A__fa
#
# class B(A):
#     def __fa(self):
#         print('from B')
#
# b=B()
# b.test()




#用来计算类被实例化的次数
# def get_no_(cls_obj):
#     return cls_obj.times_inst
#通常情况下，类实例是解释器自动调用类的__init__()来构造的，通常情况下，类实例是解释器自动调用类的__init__()来构造的
class Exm_cls:
    #实例化次数的初始值为0
    times_inst = 0
    #类被实例化一次，就+1
    def __init__(self):
        Exm_cls.times_inst +=1
    #在内部定义这个函数，并且把他绑定到类
    @classmethod
    def get_no_(cls):
        return cls.times_inst
    @staticmethod
    def show_type():
        fn = classmethod(Exm_cls.get_no_)
        print(type(fn))
exm1 = Exm_cls()
exm2 = Exm_cls()
print(Exm_cls.get_no_())
print(Exm_cls.show_type())
# print(get_no_(Exm_cls))











