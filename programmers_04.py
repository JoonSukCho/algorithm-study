

s, n = input().strip().split(' ')
n = int(n)

print(len(s))
if len(s) < n and (n - len(s)) % 2 == 0:
    print(s.ljust(n))
    print(s.center(n))
    print(s.rjust(n))
else:
    pass
