import socket
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#买手机
phone.bind(('127.0.0.1',8080)) #绑定手机卡

phone.listen(5) #开机　５次？

print('starting......')
while True:#链接循环
    conn,addr=phone.accept() #等电话链接

    print('电话线路是',conn)
    print('客户端的手机号',addr)

    while True:#通信循环
        try: #应对windows　客户端异常
            data=conn.recv(1024) #收消息 ?1024
            if not data:break #应对linux客户端终端死循环
            print('客户端发来的消息是',data)

            conn.send(data.upper())
        except Exception:
            break

    conn.close()

phone.close()