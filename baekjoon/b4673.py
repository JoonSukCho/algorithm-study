# 완


def d(n):
    total = 0
    strN = list(str(n))

    for i in strN:
        total += int(i)

    total += n

    return total


i = 0
aa = []
for i in range(10000):
    aa.append(i)

j = 0
while j < 10000:
    if d(j) in aa:
        aa.remove(d(j))
    j += 1

for i in aa:
    print(i)
