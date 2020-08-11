

a = input().split('-')

num_list = []

for i in a:
    num = 0
    s = i.split('+')
    for j in s:
        num += int(j)

    num_list.append(num)

n = num_list[0]

for i in range(1, len(num_list)):
    n -= num_list[i]

print(n)
