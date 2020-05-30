D, N = map(int, input().split())

count = 0
for i in range(1, 10 ** 7):
    tmp = i
    flag = True
    div_count = 0
    for j in range(3):
        if tmp%100 == 0:
            tmp = tmp // 100
            div_count += 1

    if div_count == D:
        count += 1

    if count == N:
        print(i)
        break