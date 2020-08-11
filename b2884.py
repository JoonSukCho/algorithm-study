

h, m = map(int, input().split(' '))


m = m - 45
if m < 0:
    h = h - 1

    if h < 0:
        h = 23

    m = 60 + m
    print(h, m)
else:
    print(h, m)
