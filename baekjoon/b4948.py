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

while 1:

    n = int(input())
    
    if n == 0:
        break

    total = 0
    for i in range(n, 2 * n + 1):
        total += sosu(i)
    print(total)