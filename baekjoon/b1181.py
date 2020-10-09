


n = int(input())

w_list = []

for _ in range(n):
    
    word = str(input())
    word_count = len(word)

    w_list.append((word_count, word))


w_list = list(set(w_list))

w_list.sort()

for word_count, word in w_list:
    print(word)

