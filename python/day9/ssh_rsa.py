# Author: Jason Lu

import paramiko

private_key = paramiko.RSAKey.from_private_key_file("xxx.txt")

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname='10.0.031', port=52113, username='root', pkey=private_key)

# 执行命令
stdin, stdout, stderr = ssh.exec_command('df; ifconfig')
result = stdout.read()
print(result.decode())

stdin, stdout, stderr = ssh.exec_command('ifconfig')
result = stdout.read()
print(result.decode())


ssh.close()
