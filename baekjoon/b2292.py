

# 늘어나는 갯수?
# 1, 6, 12, 18, 24, ...


n = int(input())

i = 1
a = []
index = 0
x = 1

while 1:
    a.append(i)
    i = i + (6 * x)

    if n == 1:
        print(1)
        break
    if a[index] >= n:
        print(index + 1)
        break
    index += 1
    x += 1


#            지나가는 최소 경로
# 2 ~ 7 = 6개 - 2개
# 8 ~ 19 = 12개 - 3개
# 20 ~ 37 = 18개 - 4개
# 38 ~ 61 = 24개 - 5개
# 62 ~  = 30개 -  6개...
