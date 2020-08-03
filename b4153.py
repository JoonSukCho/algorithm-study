

while 1:
    a, b, c = map(int, input().split())

    if a == 0 and b == 0 and c == 0:
        break
    
    triArr = [a, b, c]
    
    heru = max(triArr)
    triArr.remove(heru)

    if heru ** 2 == triArr[0] ** 2 + triArr[1] ** 2:
        print('right')
    else :
        print('wrong')    
