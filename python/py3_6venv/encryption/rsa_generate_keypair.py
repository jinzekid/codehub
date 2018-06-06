# Author: Jason Lu
# RSA 是 Ron Rivest、Adi Shamir、Len Adleman 于 1977 年发明的加密算法。
# 公钥加密系统在加密和解密时分别使用不同的密钥。RSA 等就是公钥加密算法
# 在公钥加密系统中，加密使用公钥(Public key)，解密使用私钥(Private key)。
# 这两种密钥 都需要通过算法生成。
# 公钥和私钥的密钥对可以通过 ssh-keygen 命令或 openssl 命令来创 建，
# 不过我们这里要学习的是用 PyCrypto 生成密钥的方法。

from Crypto.PublicKey import RSA
from Crypto import Random

INPUT_SIZE = 1024

def main():
    random_func = Random.new().read #产生随机数的函数
    key_pair = RSA.generate(INPUT_SIZE, random_func) #生成密钥对
    private_pem = key_pair.exportKey() #获取pem格式的私钥
    public_pem = key_pair.publickey().exportKey() #获取pem格式的公钥

    with open('master-public.pem', 'w') as f:
        f.write(public_pem.decode())

    with open('master-private.pem', 'w') as f:
        f.write(private_pem.decode())


    print(private_pem.decode())
    print(public_pem.decode())

if __name__ == '__main__':
    main()
