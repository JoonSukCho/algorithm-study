

# def sosu(num):
#     i = 2
#     if num == 2:
#         return 1
#     if num == 1:
#         return 0
#     while num > i:
#         mod = num % i
#         i += 1
#         print(i)

#         if mod == 0:
#             return 0
#         else:
#             return 1
#     return 0


# n = int(input())
# li = list(map(int, input().split()))

# count = 0

# if len(li) == n:
#     for i in li:
#         count += sosu(i)
# else:
#     pass
# print(count)

n = int(input())
li = list(map(int, input().split()))


def sosu(num):
    if num == 1:
        return 0
    if num == 2:
        return 1

    for i in range(2, num):
        if num % i == 0:
            return 0
    return 1


count = 0

if len(li) == n:
    for i in li:
        count += sosu(i)
else:
    pass
print(count)
