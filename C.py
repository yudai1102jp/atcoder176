N = int(input())

A_list = [int(i) for i in input().split()]
pre = 0
count = 0
for p in A_list:
    if pre > p:
        count += pre - p
    else:
        pre = p
print(count)
