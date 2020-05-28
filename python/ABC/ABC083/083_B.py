N, A, B = map(int, input().split())
res = 0
for i in range(1, N+1):
    sum1 = 0
    for j in str(i):
        sum1 += int(j)
    if A <= sum1 <= B:
        res += i

print(res)
