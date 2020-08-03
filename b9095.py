

def total(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return total(n - 3) + total(n - 2) + total(n - 1)


k = int(input(":"))


for i in range(k):
    n = int(input("n :"))

    print(total(n))


# total(5) = total(2) + total(3) + total(1) + total(2) + total(3)
# total(4) =
