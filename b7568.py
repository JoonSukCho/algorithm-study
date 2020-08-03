
xlist = []
ylist = []
rank = []
n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    xlist.append(x)
    ylist.append(y)

count = 1
for i in range(n):
    count = 1
    for j in range(n):
        if i == j:
            pass

        elif xlist[i] <= xlist[j] and ylist[i] <= ylist[j]:
            count += 1
    rank.append(count)

print(rank)


# 0 1
# 0 2
# 1 0
# 1 2
# 2 0
# 2 1
