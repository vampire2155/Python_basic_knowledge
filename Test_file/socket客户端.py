from socket import socket
#创建socket对象    ---也即创建实例
sk = socket()    #创建客户端套接字

# 尝试连接服务器
sk.connect(('127.0.0.1',12345))
client_input = input('Please input >>>')
#客户端发送数据
sk.sendall(client_input.encode('utf-8'))

#接受服务端响应的数据
data = sk.recv(1024)   # 接收小于 1024 字节的数据
print ('服务端：',data.decode('utf-8'))

#关闭客户端套接字
sk.close()


