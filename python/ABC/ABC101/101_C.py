N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = 1
tmp = N - K
ans += tmp // (K - 1)

if tmp%(K - 1) != 0:
    ans += 1

print(ans)