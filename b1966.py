

size = 7
pop = 0
pop_check = False
candies = []

for i in range(size):
    candy_line = input().split(' ')
    candies.append(candy_line)


def check_color(w, h, color, history):
    if w < 0 or h < 0 or w >= size or h >= size:
        return -1

    for his in history:
        if his[0] == w and his[1] == h:
            return -1
