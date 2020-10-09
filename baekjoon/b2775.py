



t = int(input())


for _ in range(t):
    k = int(input())
    n = int(input())

    v = [i for i in range(1, n + 1)]

    for _ in range(k):
        for j in range(1, n):
            v[j] += v[j - 1]
    print(v[n - 1])