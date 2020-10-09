
import sys

lotto = list(map(int, sys.stdin.readline().split()))
juhee = list(map(int, sys.stdin.readline().split()))
bonus = lotto.pop()

second = False
correct = 0

for j in juhee:
    for l in lotto:
        if j == l:
            correct += 1

if bonus in juhee:
    second = True


if correct == 6:
    print(1)
elif correct == 5 and second == True:
    print(2)
elif correct == 5:
    print(3)
elif correct == 4:
    print(4)
elif correct == 3:
    print(5)
elif correct <= 2:
    print(0)
