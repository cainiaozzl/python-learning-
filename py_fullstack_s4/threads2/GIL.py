import time



def cal(n):
    sum=0
    for i in range(n):
       sum+=i

s=time.time()

import threading


t1=threading.Thread(target=cal,args=(50000000,))
t2=threading.Thread(target=cal,args=(50000000,))

t1.start()
t2.start()
t1.join()
t2.join()

# cal(50000000)
# cal(50000000)

print("time",time.time()-s)
