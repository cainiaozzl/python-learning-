#作业:远程交互输入命令,并显示结果
import socket,struct

phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.connect(('127.0.0.1',8080))

while True: #通信循环
    #发消息
    cmd=input('>>:').strip()
    if not cmd:continue
    phone.send(bytes(cmd,encoding='utf-8'))

    #收报头
    baotou=phone.recv(4)
    data_size=struct.unpack('i',baotou)[0]

    #收消息
    recv_size=0
    recv_data=b''
    while recv_size < data_size:
        data=phone.recv(1024)
        recv_size+=len(data)
        recv_data+=data

    print(recv_data.decode('utf-8'))

   # print(data.decode('utf-8')) #若windows则用gbk解码

phone.close()
