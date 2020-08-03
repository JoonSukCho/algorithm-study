

n = int(input())

profile = []

for i in range(n):
    
    age, name = map(str, input().split())

    profile.append((int(age), i, name))


profile.sort()

for age, i, name in profile:
    print(age, name)