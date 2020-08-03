
#  완
c = int(input())
oArr = []
for i in range(c):
    ox = input()

    oArr = ox.split('X')
    score = 0
    for j in oArr:
        for k in range(len(j)):
            score += k + 1
    print(score)
