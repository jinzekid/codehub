# Author: Jason Lu

import paramiko

transport = paramiko.Transport(('hostname', 22))
transport.connect(username='wupeiqi', password='123')
sftp = paramiko.SFTPClient.from_transport(transport)

sftp.put('/tmp/location.py', '/tmp/test.py')
sftp.get('remove_path', 'local_path')

transport.close()