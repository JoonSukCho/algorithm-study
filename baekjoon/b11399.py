
import sys

n = int(sys.stdin.readline().strip())
time_list = list(map(int, sys.stdin.readline().split()))
time_list.sort()

total = 0
for i in range(len(time_list)):
    for j in range(i + 1):
        total += time_list[j]

print(total)
