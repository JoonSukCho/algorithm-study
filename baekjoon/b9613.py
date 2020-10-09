import time
import sys


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


t = int(input("t : "))

for _ in range(t):
    n = list(map(int, input("n : ").split()))
    count = len(n)
    total = 0

    for i in range(1, count - 1):
        for j in range(i + 1, count):
            total += gcd(n[i], n[j])
    print(total)


#
