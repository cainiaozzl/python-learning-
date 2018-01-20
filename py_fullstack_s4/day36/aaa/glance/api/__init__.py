print('api包的init文件')
__all__=['x','y','policy','versions']
from . import policy
x=1
y=2
# policy=123123123123
# versions='123123123'


#import policy#以test.py的sys.path为准,不能在包内导入自己的模块

#绝对导入
#from glance.api import policy
# from glance.api import versions

#相对导入
#
# from . import policy,versions #推荐
#
#from ..cmd.manage import main #导入上一级目录的


# /home/zzl/PycharmProjects/py_fullstack_s4/day35/packeage/glance/api