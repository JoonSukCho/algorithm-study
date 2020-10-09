

totalArr = []

n, m = map(int, input().split())

cardNum = list(map(int, input().split()))


if len(cardNum) > n:
    pass
else :

    for i in range(0, len(cardNum)):
        for j in range(1, len(cardNum)):
            for k in range(2, len(cardNum)):
                if i != j and j != k and i != k:
                    total = cardNum[i] + cardNum[j] + cardNum[k]
                    if total <= m:
                        totalArr.append(total)

    print(max(totalArr))   

