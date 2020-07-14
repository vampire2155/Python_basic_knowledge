# -*- coding: UTF-8 -*-
import paramiko

#创建一个ssh对象
ssh = paramiko.SSHClient()

#设置连接方式
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

#连接远程linux主机， 参数分别为主机IP地址，端口号，在远程主机已经存在的用户名和密码
ssh.connect('192.168.178.129',22,'songqin','root')

#执行命令 ,exec_command 该函数的返回值是 stdin, stdout, stderr
stdin, stdout, stderr = ssh.exec_command('ifconfig')
# stdin = chan.makefile_stdin("wb", bufsize)
# stdout = chan.makefile("r", bufsize)
# stderr = chan.makefile_stderr("r", bufsize)

#打印命令的执行结果
print (stdin)
print (stdout)

#将本地文件通过sftp传送到远程服务器上，
sftp = ssh.open_sftp()
sftp.put(r'G:\Python_scripts\Python_Advanced\python实现并发.py','/home/songqin/Desktop/sftp.py')

# 通过sftp上传或者下载文件  需要本地或者服务器上的   ***文件都存在才可以***。

#将远程服务器上的文件下载到本地
sftp.get('/home/songqin/Desktop/sftp.py',r'G:\Python_scripts\Python_Advanced\download.py')

#关闭ssh服务
ssh.close()



