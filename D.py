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
                num = numdec(w, h, max_num)
                if max_num < num:
                    max_num = num
                map_num[h][w] = num

    return map_num, max_num


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
    if w < 0 or h < 0 or w >= W or h >= H:
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


def search(num):
    li = set()
    temp_li = set()
    for h in range(H):
        for w in range(W):
            if map_num[h][w] == num:
                temp_li = search_sub(w, h, num)
                li = li | temp_li
    return {num: li}


def search_sub(w, h, num):
    li_sub = []
    for i in range(-2, 3):
        for j in range(-2, 3):
            w_sub = w + i
            h_sub = h + j
            if jadge(h_sub, w_sub) not in [0, num]:
                li_sub.append(jadge(h_sub, w_sub))
    return set(li_sub)


def search_goal():
    min_count = 10**6
    start_num = map_num[start_hw[0]][start_hw[1]]
    goal_num = map_num[goal_hw[0]][goal_hw[1]]
    ava = {i+1 for i in range(max_num)}
    count = search_count(start_num, goal_num, ava)
    if min_count > count:
        min_count = count
    return min_count


def search_count(now, go, num_set, count=0):
    num_set.remove(now)
    if now == go:
        return count
    elif not num_set:
        return 10**6

    next_set = load_num[now]
    for num in next_set:
        global count_list
        count.append search_(num, go, num_set, count+1)
    if:

        return count


map_num, max_num = load()
load_num = {}
for i in range(1, max_num+1):
    dic = search(i)
    if dic:
        load_num.update(dic)
print(load())
print(load_num)

count_list = []

search_goal()
print(ava)
print(min(count_list))
