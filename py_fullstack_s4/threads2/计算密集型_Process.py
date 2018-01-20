#coding:utf8
from multiprocessing import Process
import time

def counter():
    i = 0
    for _ in range(40000000):
        i = i + 1

    return True

def main():

    l=[]
    start_time = time.time()
    #
    # for _ in range(2):
    #     t=Process(target=counter)
    #     t.start()
    #     l.append(t)
    #     #t.join()
    #
    # for t in l:
    #    t.join()

    # counter()
    # counter()

    end_time = time.time()
    print("Total time: {}".format(end_time - start_time))

if __name__ == '__main__':

    main()

