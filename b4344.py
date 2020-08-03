# 완

c = int(input())

for i in range(c):
    scoreArr = list(map(int, input().split()))

    if scoreArr[0] != len(scoreArr) - 1:
        pass

    else:
        total = 0
        for j in range(1, len(scoreArr)):
            total += scoreArr[j]
        totalAvg = total / scoreArr[0]

        count = 0
        for j in range(1, len(scoreArr)):
            if scoreArr[j] > totalAvg:
                count += 1
        avgPercent = (count / scoreArr[0]) * 100
        print(str('%.3f' % round(avgPercent, 3)) + "%")
