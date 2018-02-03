# Author: Jason Lu

import time

SLOW = 3
LIMIT = 5
WARNING = 'too bad, you picked the slow algorithm :('

def paris(seq):
    n = len(seq)

    # 方法一
    if n == 1:
        return seq[0], seq[0]

    for i in range(n):
        yield seq[i], seq[(i+1) % n]

def allUniqueSort(s):
    if len(s) > LIMIT:
        print(WARNING)
        time.sleep(SLOW)

    # 方法二
    # if len(s) == 1:
    #     return True

    strStr = sorted(s)
    for (c1, c2) in paris(strStr):
        if c1 == c2:
            return False
    return True


def allUniqueSet(s):
    if len(s) < LIMIT:
        print(WARNING)
        time.sleep(SLOW)

    return True if len(set(s)) == len(s) else False

def allUnique(s, startegy):
    return startegy(s)

def main():
    while True:
        word = None
        while not word:
            word = input('Insert word (type quit to exit) >')
            print(set(word)) #获取字符串的字符(没有重复)
            print()
            if word == 'quit':
                print('bye')
                exit()

            strategy_picked = None
            strategies = {'1': allUniqueSet, '2': allUniqueSort}
            while strategy_picked not in strategies.keys():
                strategy_picked = input('Choose strategy:[1] Use a set, [2] Sort and pair>')

                try:
                    strategy = strategies[strategy_picked]
                    print('allUnique({}): {}'.format(word, allUnique(word, strategy)))
                except KeyError as err:
                    print('Incorrect option: {}'.format(strategy_picked))

            print()

if __name__ == '__main__':
    main()
































































































