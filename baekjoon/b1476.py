

# ycount = 1

# Ecount = 1
# Scount = 1
# Mcount = 1

# nlist = list(map(int, input("year : ").split()))


# while 1:
#     if Ecount > 15:
#         Ecount = 1

#     elif Scount > 28:
#         Scount = 1

#     elif Mcount > 19:
#         Mcount = 1

#     elif nlist[0] == Ecount and nlist[1] == Scount and nlist[2] == Mcount:
#         print("year : ", ycount)
#         break

#     else:
#         ycount = ycount + 1
#         Ecount += 1
#         Scount += 1
#         Mcount += 1

E, S, M = map(int, input().split())

for i in range(1, 7981):
    if i % 15 == E or (i % 15 == 0 and E == 15):
        if i % 28 == S or (i % 28 == 0 and S == 28):
            if i % 19 == M or (i % 19 == 0 and M == 19):
                print(i)