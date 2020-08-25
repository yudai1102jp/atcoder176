N_st = str(9**200000)
num = 0
for i in N_st:
    num += int(i)

if num % 9 == 0:
    print('Yes')
else:
    print('No')
