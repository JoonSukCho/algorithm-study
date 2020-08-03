import math

def sosu(num):
    if num == 1:
        return 0
    if num == 2:
        return 1

    n = int(math.sqrt(num))
    for i in range(2, n + 1):
        if num % i == 0:
            return 0
    return 1


m, n = map(int,input().split())

for i in range(m, n + 1):
    if sosu(i):
        print(i)

