# Author: Jason Lu

import paramiko

ssh = paramiko.SSHClient()

ssh.connect(hostname='c1.salt.com', port=22, username='wupeiqi', password='123')

stdin, stdout, stderr = ssh.exec_command('df')

result = stdout.read()

ssh.close()
