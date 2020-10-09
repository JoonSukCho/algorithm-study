

import sys

num = list(map(int, sys.stdin.readline().split()))

for i in range(len(num) - 1):
    for j in range(len(num) - i - 1):
        if num[j] > num[j + 1]:
            num[j], num[j + 1] = num[j + 1], num[j]

print(num[1])
