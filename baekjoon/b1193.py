



x = int(input())


line = 1

while x > line:
    x -= line
    line += 1

print(line)
if line % 2 == 0:
    a = x
    b = line - x + 1
else :
    a = line - x + 1
    b = x

print(a, '/', b, sep='')