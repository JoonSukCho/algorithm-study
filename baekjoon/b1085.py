


x, y, w, h = map(int, input().split())


if x >= 1 and x <= w - 1 and y >= 1 and y <= h - 1:
    a = w - x 
    b = h - y
    
    aarr = [x, y, a, b]

    print(min(aarr))
else:
    pass