# 완
a = int(input())
b = int(input())
c = int(input())
strABC = str(a * b * c)
numArr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for i in numArr:
    count = 0
    for j in strABC:
        if i == j:
            count += 1
    print(count)
