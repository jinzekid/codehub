# Author: Jason Lu

import getpass

_username = 'jason'
_password = '123'

username = input("username:")
password = input("password:")
# password = getpass.getpass("password:")

print(username, password)

if _username == username and _password == password:
    print("Welcome user {name} login...".format(name=username))
else:
    print("Invalid username or password!")