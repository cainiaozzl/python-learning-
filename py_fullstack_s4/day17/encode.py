# -*- coding: utf-8 -*-
name = "中国"

print name
print [name] #windows系统安装的python解析器,默认是gbk
print [name.decode("utf-8")] #呈现现在所用的编码
#print name.decode("utf-8") #呈现unicode转化成uf-8后的编码（自动转）
gbk= name.decode("utf-8").encode("GBK") #制定转换的目标编码
print gbk
print gbk.decode("GBK").encode("gb2312") #gbk兼容ｇｂ２３１２
'''
python2.7　报错：Non-ASCII character '\xe4' in file 　, but no encoding declared;

see http://python.org/dev/peps/pep-0263/ for details
ｐｙｔｈｏｎ２
Defining the Encodingsee http://python.org/dev/peps/pep-0263/ for details
Python will default to ASCII as standard encoding if no other encoding hints are given.

py2默认编码是ASCII码，除非提前指定
./xxxpy.py #该执行方式需在文件头声明解析器
python xxxpy.py　#该执行方式不需要声明解析器

#两种声明方法如下

#１：
# coding=<encoding name>


#２：
# -*- coding: <encoding name> -*-
'''
