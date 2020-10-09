
import sys

time, point = map(int, sys.stdin.readline().split())

sPoint = int((89 - time) / 5) + 1

print(point + sPoint)
