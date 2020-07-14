from socket import socket
#创建socket对象    ---也即创建实例
sk = socket()      # 这里的socket() 是一个socket类里面的函数，是一个实例属性（特征）。

#绑定IP地址 和 端口号
sk.bind(('127.0.0.1',12345))  # bind() 函数可以传入 类型为  tuple 、str 、 bytes 。但是此处需要用 元组类型传参。

#开始TCP监听，有没有请求从客户端发过来
sk.listen()
print ('The server is started...')

#等待传入连接，在连接成功后，保持阻塞状态
#连接成功之后，会返回一个  新的套接字  （sk是旧的套接字） 和 客户端的IP地址 与端口号
# Socket又称”套接字”，应用程序通常通过”套接字”向网络发出请求或者应答网络请求，使主机间或者一台计算机上的进程间可以通讯。
conn,addr = sk.accept()

#接收从客户端发送过来的数据
data = conn.recv(1024)  # 接收小于 1024 字节的数据
print ('客户端：',data.decode('utf-8'))  #接收从客户端发送过来的数据后需要 解码

server_input = input('Please input >>>')
#发送数据
conn.sendall(server_input.encode('utf-8'))

#关闭套接字
conn.close()
sk.close()


