N = int(input())
arr = [list(map(int, input().split())) for i in range(2)]
max_sum = 0

for i in range(N):
    r = 0
    sum1 = 0
    for j in range(N):
        if j == i:
            sum1 += arr[r][j]
            r = 1
        sum1 += arr[r][j]

    if sum1 > max_sum:
        max_sum = sum1

print(max_sum)
