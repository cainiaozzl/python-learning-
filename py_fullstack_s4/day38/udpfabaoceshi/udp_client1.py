import socket

udpclient=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

server_ip_port=('127.0.0.1',8080)

udpclient.sendto('hello'.encode('utf-8'),server_ip_port)
udpclient.sendto('shibushisha'.encode('utf-8'),server_ip_port)