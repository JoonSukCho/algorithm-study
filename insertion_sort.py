
# 삽입정렬
# 시간복잡도 최선 O(n), 최악 O(n^2)

def insertion_sort(arr):

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while arr[j] > key and j >= 0:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key

    return arr


print(insertion_sort([3, 5, 4, 6, 2, 3]))
