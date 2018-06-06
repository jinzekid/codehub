# Author: Jason Lu

import configparser

# 写文件
'''
config = configparser.ConfigParser()
config["DEFAULT"] = {"ServerAliveInterval": "45",
                     "Compression": "yes",
                     "CompressionLevel": "9"}

config["bitbucket.org"] = {}
config["bitbucket.org"]["User"] = "bg"

config["topsecret.server.com"] = {}
topsecret = config["topsecret.server.com"]
topsecret["Host Port"] = "50022"
topsecret["ForwardX11"] = "no"

config["DEFAULT"]["ForwardX11"] = "yes"

with open("example.ini", "w") as configfile:
    config.write(configfile)
'''

# 读文件
'''
import configparser

config = configparser.ConfigParser()
config.sections()

config.read("example.ini")
print(config.defaults())
print(config.sections())

secionts = config.sections()
for i, v in enumerate(secionts):
    print(v)

print(config["bitbucket.org"]["User"])
'''

# 删除配置文件
import configparser

config = configparser.ConfigParser()

config.read("example.ini")
sec = config.remove_section("bitbucket.org")
config.write(open("examplebak.ini", "w"))



