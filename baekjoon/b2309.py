

klist = []
klistTotal = 0
total = 0

for _ in range(0, 9):
    klist.append(int(input()))

for i in range(0, 9):
    klistTotal += klist[i]


for i in range(0, 9):
    for j in range(1, 9):
        total = klistTotal - (klist[i] + klist[j])
        if total == 100:
            a = klist[i]
            b = klist[j]
            break


klist.remove(a)
klist.remove(b)
klist.sort()

for i in klist:
    print(i)
