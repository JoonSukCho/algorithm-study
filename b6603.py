from itertools import combinations


while 1:
    k = list(map(int, input().split()))

    if k[0] == 0:
        break

    if k[0] == len(k) - 1:
        k.remove(k[0])

        kc = combinations(k, 6)

        print(list(kc))
