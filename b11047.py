import sys


n, k = map(int, sys.stdin.readline().split())

coin_list = []
for _ in range(n):
    coin = int(sys.stdin.readline())
    coin_list.append(coin)


coin_count = 0
mod = 0
for i in reversed(range(len(coin_list))):
    mod = k % coin_list[i]
    if mod < k:
        coin_count += (k - mod) / coin_list[i]
        k = mod

print(int(coin_count))
