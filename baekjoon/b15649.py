

n, m = map(int, input().split())


num_list = [i + 1 for i in range(n)]
check_list = [False] * n

arr = []

def dfs(cnt):
    if (cnt == m):
        print(*arr)
        return
    
    for i in range(0, n):
        if(check_list[i]):
            continue

        check_list[i] = True
        arr.append(num_list[i])
        print(cnt, "번 함수")
        dfs(cnt + 1)

        print(cnt, "번 pop")
        arr.pop()

        check_list[i] = False

dfs(0)

# n = 3, m = 2
# num_list = [1, 2, 3]
# arr = [1, 2]