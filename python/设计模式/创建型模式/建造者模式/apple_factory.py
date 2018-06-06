# Author: Jason Lu

MINI14 = '1.4GHz Mac mini'

class AppleFactory:
    class MacMini14:
        def __init__(self):
            self.memory = 4
            self.hdd = 500
            self.gpu = 'Inter HD Graphics 5000'

        def __str__(self):
            info = ('Model: {}'.format(MINI14),
                    'Memory: {}'.format(self.memory),
                    'Hard Disk: {}'.format(self.hdd),
                    'Graphics Card: {}'.format(self.gpu))
            return '\n'.join(info)

    def build_computer(self, model):
        if (model == MINI14):
            return self.MacMini14()
        else:
            print("I don't know how to build {}".format(model))


if __name__ == '__main__':
    afac = AppleFactory()
    mac_mini = afac.build_computer(MINI14)
    print(mac_mini)



