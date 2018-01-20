#name = "Alex\teee Li"
name = "my name is {0},i am {1} years old"
name2 = "my name is {name},i am {age} years old"

print(name2.lstrip("My name"))
print(name2.swapcase()) #大小写互换

print( '|||'.join(['alex','jack','rain'])) #把列表拼接成字符串
print(name2.ljust(50,'-'))
print(name2.rjust(50,'-'))

print(name2.lower()) #大写变小写
# print('ala'.isalnum()) #a-zA-Z 0-9
# print('10354243'.isdecimal()) #是不是一个正整数
# print('aA'.isalpha()) #是不是字母
# print('a'.isidentifier())  #identifier 关键字,是不是合法的关键字\变量名
#
# print('A'.islower())
# print('A'.isupper())
# print('123.3'.isnumeric()) #基本上没什么用
# print('a'.isprintable()) #能否打印
# print(' '.isspace()) #是不是空格
# print('Today Headline'.istitle()) #是否为英文标题

# print(name.capitalize())#首字母大写

# print(name.casefold()) #大写变小写
#
# print(name.center(50,'*'))
# print(name.count('e',3,7))
#
# print(name.endswith("Li"))
# print(name.expandtabs(30)) #设置\t的长度
#
# print(name.find("sdf",3)) #返回找的第一个值的索引，找不到就返回-1
# print(name.format("Alex",22))
# print(name2.format(name="Alex",age=22)) #格式化输出
#
# print(name2.format_map({'name':'Alex','age':23}))

print(name2.index('age'))

IN = "abcde"
OUT = "12345"

trans_table = str.maketrans(IN,OUT) #translate
print(name2.translate(trans_table)) #翻译字符串
print(name.zfill(50)) #没啥用
print(name2.replace('name','NAME',1))