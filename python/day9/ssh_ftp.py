# Author: Jason Lu

import paramiko

private_key = paramiko.RSAKey.from_private_key_file("xxx.txt")

transport = paramiko.Transport(('hostname', 22))
transport.connect(username='wupeiqi', pkey=private_key)


sftp = paramiko.SFTPClient.from_transport(transport)

sftp.put('/tmp/location.py', '/tmp/test.py')
sftp.get('remove_path', 'local_path')

transport.close()