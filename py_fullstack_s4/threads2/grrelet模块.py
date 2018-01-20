# from greenlet import greenlet
#
#
# def test1():
#     print(12)
#
#     gr2.switch()
#     print(34)
#     gr2.switch()
#
#
# def test2():
#     print(56)
#     gr1.switch()
#     print(78)
#
#
# gr1 = greenlet(test1)
# gr2 = greenlet(test2)
#
# gr1.switch()


#gevent模块

# import gevent
# import time
#
# def foo():
#     print("running in foo")
#     gevent.sleep(2)
#     print("switch to foo again")
#
# def bar():
#     print("switch to bar")
#     gevent.sleep(5)
#     print("switch to bar again")
#
# start=time.time()
#
# gevent.joinall(
#     [gevent.spawn(foo),
#     gevent.spawn(bar)]
# )
#
# print(time.time()-start)

from gevent import monkey
monkey.patch_all()

import gevent
from urllib import request
import time

def f(url):
    print('GET: %s' % url)
    resp = request.urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))

start=time.time()

# gevent.joinall([
#         gevent.spawn(f, 'https://itk.org/'),
#         gevent.spawn(f, 'https://www.github.com/'),
#         gevent.spawn(f, 'https://zhihu.com/'),
# ])

f('https://itk.org/')
f('https://www.github.com/')
f('https://zhihu.com/')


print(time.time()-start)