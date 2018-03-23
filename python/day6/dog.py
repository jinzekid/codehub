#!/usr/local/bin/python3

class Dog(object):
    def __init__(self, name):
        self.name = name

    def bulk(self):
        print(self.name, "wang wang wang!")


if __name__ == '__main__':
    d1 = Dog("d1")
    d2 = Dog("d2")
    d3 = Dog("d3")

    d1.bulk()
    d2.bulk()
    d3.bulk()


