
# 버블정렬
# 시간복잡도 O(n^2)
arr = []
for _ in range(6):
    arr.append(int(input()))


for i in range(len(arr) - 1):
    for j in range(len(arr) - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

for i in arr:
    print(i)
