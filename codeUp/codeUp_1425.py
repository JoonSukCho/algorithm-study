
import sys
import math

n, c = map(int, sys.stdin.readline().split())
stu = list(map(int, sys.stdin.readline().split()))


def bubble_sort(num):
    for i in range(len(num) - 1):
        for j in range(len(num) - i - 1):
            if num[j] > num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]

    return num


sorted_stu = sorted(stu)

for i in range(len(sorted_stu)):
    print(sorted_stu[i], end=' ')
    if i == c - 1:
        print()
