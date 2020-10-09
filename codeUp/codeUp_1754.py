
import sys

a, b = sys.stdin.readline().strip().split()

if len(a) < len(b):
    print(a, b)
elif len(a) > len(b):
    print(b, a)
else:
    for i in range(len(a)):
        if int(a[i]) > int(b[i]):
            print(b, a)
            break
        elif int(a[i]) < int(b[i]):
            print(a, b)
            break
        else:
            pass
