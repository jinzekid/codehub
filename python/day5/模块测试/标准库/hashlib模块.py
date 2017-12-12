# Author: Jason Lu

import hashlib

m = hashlib.md5()
m.update(b"Hello")
print(m.hexdigest())
m.update(b"It's me")
print(m.hexdigest())
m.update(b"It's been a long time since last time we ...")

print(m.hexdigest())

m2 = hashlib.md5()
m2.update(b"HelloIt's me")
print(m2.hexdigest())

# ######## sha1 ########
hash = hashlib.sha1()
hash.update(b"admin")
print(hash.hexdigest())


import hmac
h = hmac.new(b"12345", "这是中文".encode(encoding="utf-8"))
print(h.digest())
print(h.hexdigest())




