
n = int(input())

name = []
score = []
for _ in range(n):
    arr = input().split()
    name.append(arr[0])
    score.append(int(arr[1]))

for i in range(len(score) - 1):
    for j in range(len(score) - i - 1):
        if score[j] > score[j + 1]:
            score[j], score[j + 1] = score[j + 1], score[j]
            name[j], name[j + 1] = name[j + 1], name[j]

print(name[len(name) - 3])
