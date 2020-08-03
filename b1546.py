# 완
n = int(input())

scoreArr = list(map(int, input().split()))
total = 0

if n != len(scoreArr):
    pass

else:
    maxScore = max(scoreArr)

    for i in range(len(scoreArr)):
        scoreArr[i] = scoreArr[i] / maxScore * 100
        total += scoreArr[i]
    print(total / n)
