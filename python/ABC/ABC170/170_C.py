X, N = map(int, input().split())
P = list(map(int, input().split()))

ans = 10 ** 5
for i in range(X - 100, X + 100 + 1):
    if i not in P:
        if ans > abs(X - i):
            ans = abs(X - i)
            tmp = i

print(tmp)