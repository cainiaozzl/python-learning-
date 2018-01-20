# egg_list=[]
# for i in range(100):
#     egg_list.append('egg%s' %i)
# print(egg_list)

# l=['egg%s' %i for i in range(100) if i >50 ]
# print(l)
#
# #三元表达式
# name = 'alex'
# name = 'egon'
#
# res='SB' if name == 'alex' else 'shuai'
# print(res)

####
l=[1,2,3,4]
s='hello'
#声明式编程
l1=[(num,s1) for num in l for s1 in s]
print(l1)

# l1=[]
# for num in l:
#     for s1 in s:
#         t=(num,s1)
#         l1.append(t)
# print(l1)

import os
g=os.walk('/tmp/test')
file_path_list=[]
for i in g:
    for j in i[-1]:
        file_path_list.append('%s/%s' %(i[0],j))

print(file_path_list)

g=os.walk('/tmp/test')

l1=['%s/%s' %(i[0],j) for i in g for j in i[-1]]
print(l1)