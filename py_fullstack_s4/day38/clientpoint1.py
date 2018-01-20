import socket
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.connect(('127.0.0.1',8080))

while True: #通信循环
    msg=input('>>:').strip()
    if not msg:continue
    phone.send(msg.encode('utf-8'))
    print('send=========>')
    data=phone.recv(1024)
    print('recved========>')
    print(data)

phone.close()
