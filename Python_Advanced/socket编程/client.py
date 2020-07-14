import socket
#创建socket对象
sk = socket.socket()
#连接指定计算机的端口
sk.connect(('127.0.0.1',12300))
#发送消息
sk.sendall(input('>>>').encode('utf8'))
#接收消息
server_info = sk.recv(1024).decode('utf8')
print (f'info from server:{server_info}')
sk.close()













