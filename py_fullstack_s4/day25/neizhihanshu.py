print(abs(-1))

# all():
# print(all(''))
# print(all((1,' ',2,None)))
# print(all(i for i in range(1,10)))

print(any([]))
print(any([None,0,'',{},1]))

res=sum(i for i in range(3))
print(res)

#bin()
print(bin(3))

print(bool(0))
print(bool(None))
print(bool(''))

#bytes()
print(bytes('hello',encoding='utf-8'))

#callable()
# def test():
#     pass
# print(callable(test))
# print(callable(sum))
#
#
# print(chr(65))
# print(ord('A'))
#
# num=1
# print(isinstance(num,int))
#
float
bool
str
tuple
dict
set
frozenset

f=frozenset({1,2,3,4})

complex
x=complex(1-2j)
print(x.real)
print(x.imag)

#dir()
l=[]
#print(dir(l))

#divmod()
print(divmod(10,3))

#enumerate
# for i in enumerate(['a','b','c','d']):
#     print(i)
#
# s='hello'
# print(hash(s))
# s='h'
# print(hash(s))
#
# a=1
# b=2
# print(id(a))
# print(id(b))
# print(a is b)

# x='a'
# y='a'
# print(id(x))
# print(id(y))
# print(x is y)


filter
map



#complie
#eval
#exec

#面向对象的内置函数:
# classmethod
# getattr()
# setattr()
#issubclass()

# salaries={
#     'egon':3000,
#     'alex':100000000,
#     'wupeiqi':10000,
#     'yuanhao':2500
# }
# print(max(salaries))
# print(max(salaries.values()))
#
# def get_value(k):
#     return salaries[k]

#print(get_value('egon'))
#print(max(salaries))

#print(max(salaries,key=get_value))
#print(get_value())
#print(max(salaries,key=lambda k:salaries[k]))
#匿名函数:
#f=lambda k:salaries[k] #===>salaries[k]
#print(f)
#print(f('egon'))

#zip()拉链函数
l1=[1,2,3]
s='hel'
for i in zip(l1,s):
    print(i)

#print(salaries.keys(),salaries.values())
#z=zip(salaries.values(),salaries.keys())
# print(z)
# for i in z:
#     print(i)

#print(max(z))

print(max('abcaabddaass','abcd'))
print(max((2,'a'),(1,'b')))

l=[3,4,1,0,9,10]
print(sorted(l,reverse=True))
s='hello abc'
print(sorted(s))

salaries={
    'egon':3000,
    'alex':100000000,
    'wupeiqi':10000,
    'yuanhao':2500
}

#print(sorted(salaries)) #默认按字典的key来排序

print(sorted(salaries,key=lambda x:salaries[x]))
print(sorted(salaries,key=lambda x:salaries[x],reverse=True))

#map
# l=[1,2,3,7,5]

#x=[for i in l]:
#print(x)
# m=map(lambda item:item**2,l)
# print(list(m))


name_l=['alex','zhengjiangF4','yuanhao','wupeiqi']
m=map(lambda name:name + 'SB',name_l)
print(list(m))


#reduce
from functools import reduce

l=list(range(100))
# print(l)
print(reduce(lambda x,y:x+y,l,100))



#filter
name_1=[
    {'name':'egon','age':18},
    {'name':'dragonFire','age':100000},
    {'name':'gaoluchuan','age':9000},
    {'name':'fsw','age':10000},
]

f=filter(lambda d:d['age'] > 100,name_1)
print(f)
for i in f:
    print(i)


print(round(10.3))

l=[1,2,3,4,5,6,7]
slice(2,4)
