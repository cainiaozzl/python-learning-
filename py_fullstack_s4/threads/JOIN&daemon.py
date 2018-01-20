import threading
from time import ctime,sleep
import time

def Music(name):

        print ("Begin listening to {name}. {time}".format(name=name,time=ctime()))
        sleep(3)
        print("end listening {time}".format(time=ctime()))

def Blog(title):

        print ("Begin recording the {title}. {time}".format(title=title,time=ctime()))
        sleep(5)
        print('end recording {time}'.format(time=ctime()))


threads = []

t1 = threading.Thread(target=Music,args=('FILL ME',))
t2 = threading.Thread(target=Blog,args=('python',))

threads.append(t1)
threads.append(t2)

if __name__ == '__main__':

    t2.setDaemon(True)
    t2.setDaemon(True)

    for t in threads:

        t.start()

    for t in threads:
        t.join()

    t1.start()
    t1.join()
    t2.start()
    t2.join()

    print ("all over %s" %ctime())