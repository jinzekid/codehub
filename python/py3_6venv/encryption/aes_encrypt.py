# Author: Jason Lu
# 通用加密算法
# AES（Advanced Encryption Standard）
from Crypto.Cipher import AES

KEY = 'testtesttesttest' #加密和解密时候使用的通用蜜钥
DATA = '0123456789123456' #数据长度为16的倍数

def main():
    aes = AES.new(KEY)
    encrypt_data = aes.encrypt(DATA)

    print(encrypt_data)
    decrypt_data = aes.decrypt(encrypt_data)
    print(decrypt_data)

if __name__ == '__main__':
    main()