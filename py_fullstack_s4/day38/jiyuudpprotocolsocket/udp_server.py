import socket

udpserver=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udpserver.bind(('127.0.0.1',8080))

while True: #通信循环
    data,client_addr=udpserver.recvfrom(1024)
    print(data.decode('utf-8'))
    print(client_addr)
    #msg=input('>>:')
    udpserver.sendto(data.upper(),client_addr)