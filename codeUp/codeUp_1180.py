
import sys

n = int(sys.stdin.readline())


def compress(num):
    num = str(num)
    newNum = int(num[1] + num[0])

    return newNum * 2


comN = compress(n)

if comN <= 100:
    if comN <= 50:
        print(comN)
        print('GOOD')
    else:
        print(comN)
        print('OH MY GOD')

else:
    comN = str(comN)
    a = int(comN[1] + comN[2])
    if a <= 50:
        print(a)
        print('GOOD')
    else:
        print(a)
        print('OH MY GOD')
