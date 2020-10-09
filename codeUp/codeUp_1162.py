

yy, mm, dd = map(int, input().split())

saju = str(yy - mm + dd)


if saju[-1] == '0':
    print('대박')
else:
    print('그럭저럭')
