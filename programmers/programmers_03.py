
num, base = map(int, input().strip().split(' '))

arr = []
for i in range(len(str(num)), 0, -1):
    arr.append(int(str(num)[i - 1]))

r = 0
for i in range(len(arr)):
    r = r + (arr[i] * base ** i)
print(r)
