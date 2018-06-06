#! /Users/jasonlu/.virtualenvs/pyven3_6/bin/python 
"""
分割字符串或文本并交互地进行分页
"""
def more(text, numlines = 15):
    lines = text.splitlines()
    while lines:
        chunk = lines[:numlines]
        lines = lines[numlines:]
        for line in chunk:
            print(line)

        if len(lines) <= 0 or input("more:(Input 'Y' or 'y' to continue)") not in ['y','Y']:
            print("Bye...")
            break


if __name__ == '__main__':
    import sys
    print(sys.argv)
    more(open(sys.argv[1]).read(), 10)



