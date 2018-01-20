import threading
from time import ctime,sleep
import time

def Music(name):

        print ("Begin listening to {name}. {time}".format(name=name,time=ctime()))
        sleep(3)
        print(threading.activeCount())
        print(threading.enumerate())
        print("end listening {time}".format(time=ctime()))


def Blog(title):

        print ("Begin recording the {title}. {time}".format(title=title,time=ctime()))
        sleep(5)
        print('end recording {time}'.format(time=ctime()))


threads = []


t1 = threading.Thread(target=Music,args=('FILL ME',),name="sub_thread")
t2 = threading.Thread(target=Blog,args=('',))

threads.append(t1)
threads.append(t2)

if __name__ == '__main__':

    t1.setDaemon(True)  # daemon：监听

    for t in threads:

        t.start()

    print ("all over %s" %ctime())