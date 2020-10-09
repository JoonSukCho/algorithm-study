
import sys

n = int(sys.stdin.readline())
k = list(map(int, sys.stdin.readline().split()))


def compare(num1, num2):
    if num1 > num2:
        return '> '
    elif num1 < num2:
        return '< '
    elif num1 == num2:
        return '= '


for i in range(len(k)):
    s = ''
    for j in range(len(k)):
        if i == j:
            pass
        else:
            s += compare(k[i], k[j])
    print('%d: ' % (i + 1) + s)
