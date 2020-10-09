



a, b, v = map(int, input().split())


Is = 0

if (v - b) % (a - b) != 0:
    Is = ((v - b) // (a - b)) + 1
else :
    Is = ((v - b) // (a - b))
print(Is)
