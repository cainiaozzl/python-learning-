# name = [1,2,3,4,['alex','rain',3]]
#
# n2 = name.copy()
# name[1] = -2
# name[4][0] = "ALEX LI"
# name[4][2] = -3
# print(name)
# print(n2)
#
#
#
#
# account = {
#     'name':'秦镇',
#     'id':1234,
#     'info' : [ 200,10 ]
# }
#
# account2 = account.copy()
# account2['name'] = "骗子"
#
# account["info"][1] += 30
#
# print(account,account2)
#

info = {}

info = info.fromkeys([1,2,3],'Test') #method 方法
print(info)