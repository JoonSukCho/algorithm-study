
import sys

h, m = map(int, sys.stdin.readline().split())

before_minute = m - 30

if before_minute < 0:
    h -= 1
    before_minute += 60

if h < 0:
    h = 23

print(h, before_minute)
