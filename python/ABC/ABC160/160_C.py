K, N = map(int, input().split())
A = list(map(int, input().split()))

tmp = [0 for _ in range(N)]
for i in range(N-1):
    tmp[i] = A[i+1] - A[i]

tmp[-1] = K - A[-1] + A[0]

print(K - max(tmp))