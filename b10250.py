
# h = 층 수
# w = 한 층의 방 수
# n = 몇 번째 손님
# n번째 손님에게 배정되어야 하는 방 번호


t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())
    r = []
    for i in range(1, w + 1):
        for j in range(1, h + 1):
            r.append(j * 100 + i)

    print(r[n - 1])
# print(r)