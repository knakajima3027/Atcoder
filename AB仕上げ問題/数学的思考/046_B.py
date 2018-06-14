N, K = map(int, input().split())

n = 1

for i in range(1, N+1):
    if i == 1:
        n = n*K
    else:
        n = n*(K-1)

print(n)
