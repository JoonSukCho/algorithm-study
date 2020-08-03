


def fibonacci(n):
    if n == 0 :
        zeroCnt = zeroCnt + 1
        return 0
    elif n == 1:
        oneCnt = oneCnt + 1
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)



t = int(input())

for _ in range(t):
    n = int(input())

    for i in range(n, 1, -1):
        print(i)        


# fiboArr = [0 for i in range(41)]

# fiboArr[0] = 0
# fiboArr[1] = 1

# for i in range(2, len(fiboArr)):
#     fiboArr[i] = fiboArr[i - 2] + fiboArr[i - 1]

    


