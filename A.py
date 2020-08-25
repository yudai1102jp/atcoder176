[N, X, T] = [int(i) for i in input().split()]
count = 0
time = 0
while N > count:
    count += X
    time += T

print(time)
