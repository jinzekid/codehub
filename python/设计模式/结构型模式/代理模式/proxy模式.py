# Author: Jason Lu

class SensitiveInfo:
    def __init__(self):
        self.users = ['nick', 'tom', 'ben', 'mike']

    def read(self):
        print('There are {} users: {}'.format(len(self.users), ' '.join(self.users)))

    def add(self, user):
        self.users.append(user)
        print('Added user {}'.format(user))

    def remove(self, user):
        if user in self.users:
            self.users.remove(user);
            print('Remove user {}'.format(user))


class Info:
    '''SensitiveInfo的保护代理'''

    def __init__(self):
        self.protected = SensitiveInfo()
        self.secret = '0xdeadbeef'

    def read(self):
        self.protected.read()

    def add(self, user):
        sec = input('What is the secret?')
        self.protected.add(user) if sec == self.secret else print("That's wrong!")

    def remove(self, user):
        sec = input('What is the secret?')
        self.protected.remove(user) if sec == self.secret else print("That's wrong!")

def main():
    info = Info()

    while True:
        print('1. read list |==| 2. add user |==| 3. remove |==| 4. quit')
        key = input('choose option:')
        if key == '1':
            info.read()
        elif key == '2':
            name = input('choose username:')
            info.add(name)
        elif key == '3':
            name = input('choose username:')
            info.remove(name)
        elif key == '4':
            exit()
        else:
            print('unknown option: {}'.format(key))


if __name__ == '__main__':
    main()
