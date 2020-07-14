import socket
sk = socket.socket()
sk.connect(('127.0.0.1',21567))
myName = 'testName'

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
while True:
    data = input('Please input>>>')
    data = handleData(data)
    sk.sendall(bytes(data,encoding='utf8'))
    recv_data = sk.recv(1024)
    print (str(recv_data,encoding='utf8'))
