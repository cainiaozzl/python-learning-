#作业:远程交互输入命令
import socket,time
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#买

ip_port=('127.0.0.1',8080)#绑定手机卡
phone.bind(ip_port)
phone.listen(5) #开机　５次
conn,addr=phone.accept()

#data1=conn.recv(1024)
data1=conn.recv(1) #b'h'

time.sleep(5)

data2=conn.recv(1024) #b'elloworld'


print('第一个包',data1)
print('第二个包',data2)

