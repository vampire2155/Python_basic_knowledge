# coding=utf8
import sys
from socket import socket

HOST = '127.0.0.1'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)
sk = socket()
sk.bind(ADDR)
sk.listen(5)
def handleData(data):
    data_len = len(data)
    if len(str(data_len)) < 4:
        data_len = ''.join(['0'* (4-len(str(data_len))),str(data_len)])
    else:
        data_len = str(data_len)
    #处理消息的第二部分
    if data == 'testName':
        data_type = '1'
    else:
        data_type = '2'
    return '|'.join([data_len,data_type,data])

print('等待客户端连接...')
while True:
    #阻塞式等待连接请求
    conn, err = sk.accept()
    while True:
        try:
            recv_data = conn.recv(1024)
            print (str(recv_data,encoding='utf8'))
            data = input('pls input>>>')
            data = handleData(data)
            conn.sendall(bytes(data,encoding='utf8'))
        except:
            print ('连接意外中断')
            break