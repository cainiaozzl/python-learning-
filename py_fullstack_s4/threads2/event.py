import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s',)


def worker(event):
    logging.debug('Waiting for redis ready...')

    while not event.isSet():
        logging.debug("wait.......")
        event.wait(3)   # if flag=False阻塞，等待flag=true继续执行


    logging.debug('redis ready, and connect to redis server and do some work [%s]', time.ctime())
    time.sleep(1)

def main():

    readis_ready = threading.Event()  #  flag=False
    t1 = threading.Thread(target=worker, args=(readis_ready,), name='t1')
    t1.start()

    t2 = threading.Thread(target=worker, args=(readis_ready,), name='t2')
    t2.start()

    logging.debug('first of all, check redis server, make sure it is OK, and then trigger the redis ready event')

    time.sleep(6) # simulate the check progress
    readis_ready.set()  # flag=Ture


if __name__=="__main__":
    main()