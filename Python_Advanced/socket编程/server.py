import socket
#创建socket对象
sk = socket.socket()
#绑定端口和IP地址
sk.bind(('127.0.0.1',12300))  #需要使用tuple传参
#监听
sk.listen()
print ('server is ready...')
#accept  阻塞中，直到有客户端连接过来
conn,addr = sk.accept()
# print (sk.accept())

#接收消息
client_info = conn.recv(1024).decode('utf8')
print (f'info from client:{client_info}')
#发送消息
conn.sendall(input('>>>').encode('utf8'))
#关闭socket对象
conn.close()
sk.close()



