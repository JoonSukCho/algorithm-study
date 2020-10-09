
t = int(input())

for i in range(t):
    a, b = input().split()
    a = int(a)
    b = int(b)
    mul = a * b

    while 1:
        mod = a % b
        a = b
        b = mod

        if mod == 0:
            chlth = a
            chleo = mul / a
            break

    print(int(chleo))

