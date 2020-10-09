

n = int(input())


def fibo(n):

    if n == 0:
        i = 0
        return i

    if n == 1:
        i = 1
        return i

    return fibo(n - 1) + fibo(n - 2)


print(fibo(n))
