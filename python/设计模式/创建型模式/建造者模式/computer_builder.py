# Author: Jason Lu

class Computer:
    def __init__(self, serial_number):
        self.serial_number = serial_number
        self.memory = None
        self.hdd = None
        self.gpu = None

    def __str__(self):
        info = ('Memory: {}GB'.format(self.memory),
                'Hard Dish: {}GB'.format(self.hdd),
                'Graphics Card: {}'.format(self.gpu))

        return '\n'.join(info)


class ComputerBuilder:
    def __init__(self):
        self.computer = Computer('AG23385193')

    def configuer_memory(self, amount):
        self.computer.memory = amount

    def configuer_hdd(self, amount):
        self.computer.hdd = amount

    def configuer_gpu(self, gpu_mode):
        self.computer.gpu = gpu_mode


class HardwareEngineer:
    def __init__(self):
        self.builder = None

    def construct_computer(self, memory, hdd, gpu):
        self.builder = ComputerBuilder()
        self.builder.configuer_memory(memory)
        self.builder.configuer_hdd(hdd)
        self.builder.configuer_gpu(gpu)
        # [step for step in (self.builder.configuer_memory(memory),
        #                    self.builder.configuer_hdd(hdd),
        #                    self.builder.configuer_gpu(gpu))]

    @property
    def computer(self):
        return self.builder.computer


def main():
    engineer = HardwareEngineer()
    engineer.construct_computer(memory='4', hdd=512, gpu='GTX 650')
    computer = engineer.computer
    print(computer)

if __name__ == '__main__':
    main()