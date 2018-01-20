import socket

sock=socket.socket()
sock.bind(("127.0.0.1",8080))

sock.listen(5)

while True:
    conn,addr=sock.accept()

    data=conn.recv(1024)
    print("data")

    conn.send(b"http /1.1 \r\nyuan")

    conn.close()