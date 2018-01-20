# # class Foo:
# #     def __init__(self):
# #         self.test=123
# #     @property
# #     def test(self):
# #         print('from test')
# #
# #     @test.setter
# #     def test(self,value):
# #         print('from test setter',value)
# #
# #
# #     @test.deleter
# #     def test(self):
# #         print('from test deleter')
# # f=Foo()
# # f.test
# # del f.test
#
#
# class People:
#     def __init__(self,name,x):
#         self.name=name
#         self.__SEX=x
#
#     @property
#     def sex(self):
#         return self.__SEX #self._People__SEX
#
#     @sex.setter
#     def sex(self,value):
#         if not isinstance(value,str):
#             raise TypeError('must be str')
#         self.__SEX=value
#
#     @sex.deleter
#     def sex(self):
#         raise Exception('不让删除')
#         # del self.__SEX
#
# p=People('egon','male')
# # print(p.sex)
# #
# # p.sex='female'
# # print(p.sex)
# # del p.sex
# # print(p.sex)
#
# # p.sex=123
# # del p.sex
#
#
#
# class People:
#     def __init__(self,name,age,height,weight):
#         self.name=name
#         self.age=age
#         self.height=height
#         self.weight=weight
#     @property
#     def bodyindex(self):
#         return self.weight/(self.height**2)
#
#
# p=People('egon',18,1.80,90)
# print(p.bodyindex)
# p.height=1.85
# print(p.bodyindex)
