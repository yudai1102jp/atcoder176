[H, W] = [int(i) for i in input().split()]

start_hw = [int(i) for i in input().split()]
goal_hw = [int(i) for i in input().split()]

map = []

for h in range(H):
    map.append(input())
map_num = [[0] * W for i in range(H)]


def load():
    global map_num
    num = max_num = 0
    for h in range(H):
        for w in range(W):
            if map[h][w] == '.':
                print(w, h)
                num = numdec(w, h, max_num)
                if max_num < num:
                    max_num = num
                map_num[h][w] = num

    return map_num


def numdec(w, h, num):
    up_wh = [w, h-1]
    left_wh = [w-1, h]

    up_num = jadge(*up_wh)
    left_num = jadge(*left_wh)

    if up_num == 0 and left_num == 0:
        return num+1
    elif up_num == 0 and left_num != 0:
        return left_num
    elif up_num != 0 and left_num == 0:
        return up_num
    elif up_num == left_num:
        return left_num
    elif up_num > left_num:
        convert(up_num, left_num)
        return left_num
    elif up_num < left_num:
        convert(left_num, up_num)
        return up_num


def jadge(w, h):
    if w < 0 or h < 0 or w > W or h > H:
        return 0
    else:
        return map_num[h][w]


def convert(befornum, afternum):
    global map_num
    for h in range(H):
        for w in range(W):
            if map_num[h][w] == befornum:
                map_num[h][w] = afternum
    return 0


map_num = load()
print(load())
