#作业:远程交互输入命令,并显示结果
import time
import socket

phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip_port=('127.0.0.1',8080)
phone.connect(ip_port)


phone.send('Hello World'.encode('utf-8'))

phone.send('SB'.encode('utf-8'))

