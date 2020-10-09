

height = list(map(int, input().split()))

flag = 'PASS'
for h in height:
    if h <= 170:
        flag = 'CRASH'

print(flag)
