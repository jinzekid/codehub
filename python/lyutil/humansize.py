"""
格式化文件的大小
"""
SUFFIXES = {
        1000:['KB','MB','GB','TB','PB','EB','ZB','YB'],
        1024:['KiB','MiB','GiB','TiB','PiB','EiB','ZiB','YiB']
        }

def approximate_size(size, aKiloByteIs1024Bytes=True):
    '''
    Convert a file size to human-readable form.

    Keyword arguments:
    size -- file size in bytes
    aKiloByteIs1024Bytes -- if True (default), use multiples of 1024
                            if False, use multiples of 1000

    Returns: string
    '''
    if size < 0:
        raise ValueError('number must be non-nagative')

    multiple = 1024 if aKiloByteIs1024Bytes else 1000
    for suffix in SUFFIXES[multiple]:
        size /= multiple
        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix)

    raise ValueError('number too large')

if __name__ == '__main__':
    print(approximate_size(1000000000000, False))
    print(approximate_size(1000000000000))
