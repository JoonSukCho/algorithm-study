

import sys
from collections import deque

q = deque([])

n = int(sys.stdin.readline())

for i in range(1, n + 1):
    q.append(i)


while 1:
    
    if len(q) == 1:
        print(q[0])
        break

    q.popleft()
    q.append(q[0])
    q.popleft()