import sys


k = int(sys.stdin.readline().strip())

arr = []

for _ in range(k):

    n = int(sys.stdin.readline().strip())
    arr.append(n)

    if n == 0 and len(arr) > 1:
        arr.pop()
        arr.pop()


print(sum(arr))        

    

    