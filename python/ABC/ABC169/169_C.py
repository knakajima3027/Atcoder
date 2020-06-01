A, B = map(str, input().split())
A = int(A)

ans = 0
r = 4
for i in range(4):
    if i != 1:
        ans += A * int(B[i]) * (10 ** (r))
        r -= 1

print(ans // 10000)