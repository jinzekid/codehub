# Author: Jason Lu

"""Train tickets query via command-line.

 Usage:
    tickets [-gdtkz] <from> <to> <date>

 Options:
    -h --help           显示帮助菜单
    -g                  高铁
    -d                  动车
    -t                  特快
    -k                  快速
    -z                  直达

 Example:
    tickets 南京 北京 2016-07-01
    tickets -dg 南京 北京 2016-07-01

"""

from docopt import docopt
print(docopt(__doc__))


# def cli():
#     tips = '''command-line interface'''
#     arguments = docopt(__doc__, version="111")
#     print(arguments)

# if __name__ == '__main__':
#     arguments = docopt(__doc__)
#     print(arguments)

