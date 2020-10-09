
# 선택정렬
# 시간복잡도 O(n^2)

def selection_sort(li):
    for i in range(len(li) - 1):
        min_idx = i
        for j in range(i + 1, len(li)):
            if li[min_idx] > li[j]:
                min_idx = j
        if min_idx != i:
            li[i], li[min_idx] = li[min_idx], li[i]

    return li


aa = selection_sort([3, 5, 6, 1, 2, 0, 9, 3])
