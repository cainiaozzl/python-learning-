#作业:远程交互输入命令;json解决粘包问题
import socket,struct
import subprocess,json
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#买手机
#phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) #在bind前加上这一行,缩短timewait时间,解决端口占用问题

phone.bind(('127.0.0.1',8080)) #绑定手机卡

phone.listen(5) #开机　５次？

print('starting......')
while True:#链接循环
    conn,addr=phone.accept() #等电话链接

    print('',conn)
    print('client addr',addr)

    while True:#通信循环
        try: #应对windows　客户端异常
            cmd=conn.recv(1024) #收消息 ?1024
            if not cmd:break #应对linux客户端终端死循环
            res=subprocess.Popen(cmd.decode('utf8'),
                             shell=True,
                             stderr=subprocess.PIPE,
                             stdout=subprocess.PIPE)
            out_res=res.stdout.read()
            err_res=res.stderr.read()
            data_size=len(out_res)+len(err_res)
            head_dic={'data_size':data_size}
            head_json=json.dumps(head_dic)
            head_bytes=head_json.encode('utf-8')
            #part1发送报头长度
            head_len=len(head_bytes)
            conn.send(struct.pack('i',head_len))
            #part2发送报头
            conn.send(head_bytes)
            #发送数据部分
            conn.send(out_res)
            conn.send(err_res)
        except Exception:
            break

    conn.close()

phone.close()

