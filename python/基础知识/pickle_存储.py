#! /Users/jasonlu/.virtualenvs/pyven3_6/bin/python
import pickle

lyst = [60, 'A string object', 1977]


def store_list(arr, file_name):
    if len(arr) == 0:
        return 

    fileObj = open(file_name, 'wb')
    for item in arr:
        pickle.dump(item, fileObj)

    fileObj.close()


store_list(lyst, 'items2.dat')


def read_list(file_name):
    lyst = list()

    fileObj = open(file_name, 'rb')
    while True:
        try:
            item = pickle.load(fileObj)
            lyst.append(item)
        except EOFError as e:
            fileObj.close()
            break

    return lyst

ret_list = read_list('items2.dat')
print(ret_list)




