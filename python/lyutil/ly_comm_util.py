# Author: Jason Lu
def read_file(fpath):
    '''
    读取文件方法
    :param fpath: 文件路径
    :return: 返回固定大小缓冲区的文件
    '''
    BLOCK_SIZE = 1024
    with open(fpath, 'rb') as f:
        while True:
            block = f.read(BLOCK_SIZE)
            if block:
                yield block
            else:
                return

