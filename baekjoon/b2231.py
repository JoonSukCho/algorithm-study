

def divSum(num):
    total = 0

    num = str(num)

    for i in range(len(num)):
        total = total + int(num[i])

    total = total + int(num)

    return total


n = int(input())

i = 1
while 1:

    if divSum(i) == n:
        print(i)
        break

    if divSum(i) > n:
        print(0)
        break

    i = i + 1
