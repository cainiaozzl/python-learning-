import socketserver

class FtpServer(socketserver.BaseRequestHandler):
    def handle(self):
        print(self.request[0])
        print(self.request[1])
        self.request[1].sendto('嘎嘎嘎'.encode('utf-8'),self.client_address)

if __name__ == '__main__':
    obj=socketserver.ThreadingUDPServer(('127.0.0.1',8080),FtpServer)
    obj.serve_forever()