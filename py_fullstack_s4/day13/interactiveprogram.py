import getpass #python3可以直接导入，py2不行
#name = input("Input your name:")
#age = input("Input your age:")

#print(name,age)

username = input("username:")
password = getpass.getpass("password:")
print(username,password)

if username == "alex" and password == "alex123":
    print("Welcome alex!")

else:
    print("Wrong username or password!")
#该程序在ｐｙｔｈｏｎ解释器正常,在pycharm里执行有问题。

#单引号,双引号基本上没区别
#单双引号谨慎混用
#三引号可用于多行字符串，或注释