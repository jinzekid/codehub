# Author: Jason Lu
# coding: utf-8
from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64

DATA = 'hello ghost, this is a4 plian text'

PUBLIC_KEY_PEM = """-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCRWjFY+TrQp3lOnRJmbjcZ5+Hh
ner8PtJsP44bZz5Ng5BI4ycIA1codUg1mUibRs6LLC/8lAVxPf7EoYqU4U4bLkOy
w97FjDzV+VP1x3/lO84TNkHZWjaDYunXpLP5OTBbc39qVVOPqjrgI2PjDMJusJ/R
0sLU2YoEeVtTeP/hWQIDAQAB
-----END PUBLIC KEY-----"""

PUBLIC_PRIVATE_KEY_PEM = """-----BEGIN RSA PRIVATE KEY-----
MIICXQIBAAKBgQC2zbncGjhaX3PdZ3y3hnBP/DpderGYQpMYIDd9urQemx9DIflX
IA43ScJttzZhFTQ8A7DuwbfkaySC0P9XGZQR8AVc1koiYy2jqnoJqYZqWAgg3L9H
+YrJvNTDv0Jtnc1aamom9KzT2HtUPpBwhi63RjfAHXVY1kR7Ks7B0l0GjQIDAQAB
AoGBAJ5u7wa0MuMgl2rspkrpWa35DRy3mfQ8vv/J7E4r4rAkAZRNfazlO2zvoHM2
twqtNfhNuqszeg2eTqaSPLtgj9MBNmVacZUJsz9nF35e/ufaiO3/VSin4nemsqFK
S60VYZ8erW8uAtp+8j9rTSKRi88HzSHIDZJJkFUhNeJPsViBAkEAu1v03vAZZ5mA
Ysx7dSjBhGTuCON5z2nAE2IV62IzxOR+GmP47FJECoPiXAW9A/x9Q0E9cjjtPe2b
cZksYgzt+wJBAPnGgpJvT4e6dfJWazNeWYhGti38OFPnfnFxM2TofFSWtDdzAeuS
Vq7mk+7je0RCO6dlqjxB7SY+y08CgxjS3xcCQDhAF3iHZVkxQNZoxfga0F7LXpvU
j9Gx0jT/kc0lop1ObH3H3gg1erAdgGxYXLNBrunuQGB2ruOU3sJwVl7putkCQQDf
gypZC86pcMwXHgo0H5wS/OQN5oQpYSCfN2N8SybnMyz16a6wNXXocWG0BlDKVlK3
i5x4663h6ZNZkq/pyNnlAkBQXALTBXGueOd5TVuMvrAzjz7qDdTorZMYqrSZUH2D
HGHhoffB8YXKog+CgYoCJHPMVdFhT+yHnBYUImyIuCvK
-----END RSA PRIVATE KEY-----"""

def main():

    # 加密解密过程
    random_func = Random.new().read #产生随机数的函数
    with open('master-public.pem') as f:
        key = f.read()
        rsakey = RSA.importKey(key)
        cipher = Cipher_pkcs1_v1_5.new(rsakey)

        # 方法一
        # encrypted = cipher.encrypt(DATA.encode("utf-8"))
        # print(encrypted)

        # 方法二
        encrypted = base64.b64encode(cipher.encrypt(DATA.encode("utf-8")))
        print(encrypted)

    with open('master-private.pem') as f:
        key = f.read()
        rsakey = RSA.importKey(key)
        cipher = Cipher_pkcs1_v1_5.new(rsakey)

        # 方法一
        # decrypted = cipher.decrypt(encrypted, random_func)
        # print(decrypted)

        # 方法二
        decrypted = cipher.decrypt(base64.b64decode(encrypted), random_func)
        print(decrypted)


    # 签名验证过程
    with open('master-private.pem') as f:
        key = f.read()
        raskey = RSA.importKey(key)
        singer = Signature_pkcs1_v1_5.new(rsakey)
        digest = SHA.new()
        digest.update(DATA.encode("utf-8"))
        sign = singer.sign(digest)
        signature = base64.b64encode(sign)

        print("签名：{}".format(signature))

    with open('master-private.pem') as f:
        key = f.read()
        raskey = RSA.importKey(key)
        verifier = Signature_pkcs1_v1_5.new(rsakey)
        digest = SHA.new()
        digest.update(DATA.encode("utf-8"))
        is_verify = verifier.verify(digest, base64.b64decode(signature))

        print("验证: {}".format(is_verify))


    # public_key = RSA.importKey(PUBLIC_KEY_PEM) # 输入PEM格式的公钥
    # cipher = Cipher_pkcs1_v1_5.new(public_key)
    # encrypted = cipher.encrypt(DATA)
    # 会报错
    # encrypted = public_key.encrypt(DATA, random_func) #加密数据

    # print("加密后的结果:")
    # print(encrypted)
    #
    # print()
    # print("解密后的结果:")

    # private_key = RSA.importKey(PUBLIC_PRIVATE_KEY_PEM)
    # decrypted = private_key.decrypt(encrypted)
    # print(decrypted.decode())


if __name__ == '__main__':
    main()