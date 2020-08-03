

n = int(input())

fiboArr = [0 for i in range(91)]
# fiboArr = [0 for i in range(n + 1)]

fiboArr[0] = 0
fiboArr[1] = 1
fiboArr[2] = 1

for i in range(3, len(fiboArr)):
    fiboArr[i] = fiboArr[i - 2] + fiboArr[i - 1]

print(fiboArr[n])
    