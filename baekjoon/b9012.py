import sys

t = int(sys.stdin.readline().strip())



for _ in range(t):

    gh = list(input())

    s = 0

    for i in gh:
        if i == '(':
            s += 1

        elif i == ')':
            s -= 1
        
        if s < 0:
            print("NO")
            break
    
    if s > 0:
        print('NO')
    elif s == 0:
        print("YES")