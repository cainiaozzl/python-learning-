
#  调用方式1

# import threading
# import time
#
# def tingge():
#     print("听歌")
#     time.sleep(3)
#     print("听歌结束")
#
# def xieboke():
#     print("写博客")
#     time.sleep(5)
#     print("写博客结束")
#
#     print(time.time()-s)
#
# s=time.time()
#
# t1=threading.Thread(target=tingge)
# t2=threading.Thread(target=xieboke)
#
# t1.start()
# t2.start()

#  调用方式2
# import threading
# import time
#
# class MyThread(threading.Thread):
#
#     def __init__(self,num):
#         threading.Thread.__init__(self)
#         self.num=num
#
#     def run(self):
#         print("running on number:%s" %self.num)
#         time.sleep(3)

# t1=MyThread(56)
# t2=MyThread(78)
#
# t1.start()
# t2.start()
#
# print("ending")


