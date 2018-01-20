def func():
    n = 0
    while n < 5:
        yield n
        n+=1
g=func()

res=next(g)
print(res)

for i in g:
     print(i)