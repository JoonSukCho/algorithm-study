
import sys

queueArr = []

def push(num):
    queueArr.append(num)

def pop():
    try:
        print(queueArr[0])
        queueArr.pop(0)
    except:
        print(-1)

def size():
    print(len(queueArr))

def empty():
    if len(queueArr) > 0:
        print(0)
    else:
        print(1)

def front():
    if len(queueArr) < 1:
        print(-1)
    else:
        print(queueArr[0])

def back():
    if len(queueArr) < 1:
        print(-1)
    else:
        print(queueArr[len(queueArr) - 1])

n = int(sys.stdin.readline().strip())

for _ in range(n):
    
    orderNum = sys.stdin.readline().split()

    if orderNum[0] == 'push':
        push(orderNum[1])
    
    if orderNum[0] == 'pop':
        pop()
    
    if orderNum[0] == 'size':
        size()
    
    if orderNum[0] == 'empty':
        empty()
    
    if orderNum[0] == 'front':
        front()
    
    if orderNum[0] == 'back':
        back()
    