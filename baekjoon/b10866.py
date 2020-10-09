import sys

n = int(sys.stdin.readline())

deque = []
for _ in range(n):
    command_num = sys.stdin.readline().strip().split(' ')
    command = command_num[0]
    print(command_num)

    if len(command_num) > 1:
        num = command_num[1]

    if command == 'push_front':
        deque.insert(0, num)

    if command == 'push_back':
        deque.append(num)

    if command == 'pop_front':
        if len(deque) > 0:
            print(deque[0])
            deque.pop(0)
        else:
            print(-1)

    if command == 'pop_back':
        if len(deque) > 0:
            print(deque[len(deque) - 1])
            deque.pop()
        else:
            print(-1)

    if command == 'size':
        print(len(deque))

    if command == 'empty':
        if len(deque) > 0:
            print(0)
        else:
            print(1)

    if command == 'front':
        if len(deque) > 0:
            print(deque[0])
        else:
            print(-1)

    if command == 'back':
        if len(deque) > 0:
            print(deque[len(deque) - 1])
        else:
            print(-1)
