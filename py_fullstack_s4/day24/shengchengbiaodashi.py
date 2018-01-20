
# l=['egg%s' %i for i in range(100) if i >50 ]
# print(l)

# g=l=('egg%s' %i for i in range(100))
# print(g)
# print(next(g))
# for i in g:
#     print(i)


# f=open('a.txt')
# l=[]
# for line in f:
#     line=line.strip()
#     l.append(line)
# print(l)
#f.seek(0)
# l1=[line.strip() for line in f]
# print(l1)

# f.seek(0)
# g=(line.strip() for line in f)
# print(g)
# print(next(g))

# f=open('a.txt')
# g=(line.strip() for line in f)
# l=list(g)
# print(l)

# nums_g=(i for i in range(3))

#print(sum([1,2,3,4]))
# print(sum(nums_g))

#==================================================

# money_1=[]
# with open('b.txt') as f:
#     for line in f:
#         goods=(line.split())
#         res=float(goods[-1])*float(goods[-2])
#         money_1.append(res)
# print(money_1)

# f=open('b.txt')
# g=(float(line.split()[-1])*float(line.split()[-2]) for line in f)
# print(sum(g))

# res=[]
# with open('b.txt') as f:
#     for line in f:
#       l=line.split()
#       print(l)
#       d={}
#       d['name']=l[0]
#       d['price']=l[1]
#       d['count']=l[2]
#       res.append(d)
#
# print(res)




#取出单价＞１００００商品
with open('b.txt') as f:
    res=(line.split() for line in f)
    print(res)
    dic_g=({'name':i[0],'price':i[1],'count':i[2]} for i in res if float(i[1])>10000)
    print(dic_g)
    print(list(dic_g))
    #<====>
    # for i in dic_g:
    #     print(i)




#alueError: I/O operation on closed file.:
# with open('b.txt') as f:
#     d=f
# print(d)
# print(next(d))