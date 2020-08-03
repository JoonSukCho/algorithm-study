
a, b = input("a, b : ").split()

a = int(a)
b = int(b)
mul = int(a * b)
while 1:

    mod = a % b
    a = b
    b = mod

    if mod == 0:
        print( a)
        print(int(mul / a))
        break


