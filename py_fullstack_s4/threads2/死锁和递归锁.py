import threading
import time

# mutexA = threading.Lock()
# mutexB = threading.Lock()

Rlock=threading.RLock()

class MyThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):

        self.fun1()
        self.fun2()

    def fun1(self):

        Rlock.acquire()  # 如果锁被占用,则阻塞在这里,等待锁的释放

        print ("I am %s , get res: %s---%s" %(self.name, "ResA",time.time()))

        Rlock.acquire()  # count=2
        print ("I am %s , get res: %s---%s" %(self.name, "ResB",time.time()))
        Rlock.release()   #count-1

        Rlock.release()   #count-1 =0


    def fun2(self):
        Rlock.acquire()  # count=1
        print ("I am %s , get res: %s---%s" %(self.name, "ResB",time.time()))
        time.sleep(0.2)

        Rlock.acquire()  # count=2
        print ("I am %s , get res: %s---%s" %(self.name, "ResA",time.time()))
        Rlock.release()

        Rlock.release()   # count=0


if __name__ == "__main__":

    print("start---------------------------%s"%time.time())

    for i in range(0, 10):

        my_thread = MyThread()
        my_thread.start()