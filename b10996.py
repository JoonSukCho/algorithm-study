

n = int(input())


if n == 1:
    print('*')

else:
    for i in range(n):
        star = ''
        for j in range(n):
            if j % 2 == 0:
                star = star + '*'
            else:
                star = star + ' '
        print(star)
        star = ''
        for k in range(n):
            if k % 2 == 0:
                star = star + ' '
            else:
                star = star + '*'
        print(star)
