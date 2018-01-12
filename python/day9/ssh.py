# Author: Jason Lu

import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname='10.0.031', port=52113, username='root', password='123')

stdin, stdout, stderr = ssh.exec_command('df')

result = stdout.read()
print(result.decode())

ssh.close()
