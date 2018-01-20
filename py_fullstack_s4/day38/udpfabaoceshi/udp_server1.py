import socket

udpserver=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udpserver.bind(('127.0.0.1',8080))

 #udp server端，没有收全数据，在windows上会报错；在linux上运行不会有限制,报错
data,client_addr=udpserver.recvfrom(2)
print(data.decode('utf-8'))

data,client_addr=udpserver.recvfrom(2)
print(data.decode('utf-8'))
