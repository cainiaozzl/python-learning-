# i = 1
# u = 0
# while i <101 :
#     u = u + i
#     i += 1
# print(u)

# u = 0
# for i in range(0,100):
#     i += 1
#     u = u + i
# print(u)

num = 0

for i in range(100):
    if i % 2 == 0:
        num = num - i
    else:
        num = num + i
print(num)


# name=input("please input your name:")
# password=input("please input your password:")
#     if name == "david" and password == "123456":
#
#         break

count = 0   #记录用户输入密码的次数
flag = 1    #标志位
lock = []
user_pass = []
username = input('please input your name:')

#读取黑名单的内容
f = open('blacklist','r')
lock_file = f.readlines()
f.close()
#将黑名单文件内容作为列表元素追加到列表中
for i in lock_file:
    line = i.strip('\n')
    lock.append(line)

#若输入的用户名在黑名单中，如果在则给出提示信息：用户已经被锁定，请联系管理员。
if username in lock:
    print('User %s Have Been Locked.It is not allow to login,please contact Administrator.' %username)
else:
#输入的用户名不在黑名单中，则提示用户输入密码信息
    while True:
        count += 1
        passwd = input("please input your password:")
        f = open('user_information')
        user_file = f.readlines()
        #print(f.readlines())
        f.close()

        for i in user_file:
            user_pass = i.strip().split()
                #判断输入的用户名==user_pass[0] and 密码==user_pass[1],如果相等，则提示欢迎信息并退出循环，如果不相等则
                #结束本次循环
            if username == user_pass[0] and passwd == user_pass[1]:
                print('welcome user %s login !' %username)
                flag = True
                break
            else:
                continue
            #若flag为真，则用户名和密码输入正确跳出整个循环体，反之，若用户输入密码错误的次数为3，则给出提示信息：用户已经被锁定
            #并将username追加到黑名单中
        if flag is True:
            break
        else:
            if count == 3:
                print('User Have Been try 3 times,Have Been Locked')
                lock_file = open('blacklist','a')
                    #lock_file.write('Have Been Locked User:%s\n' %username)
                lock_file.write('%s\n' %username)
                lock_file.close()
                break
