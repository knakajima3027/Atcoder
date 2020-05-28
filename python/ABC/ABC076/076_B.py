N = int(input())
K = int(input())
res = 1

for i in range(N):
    res = min(res+K, res*2)

print(res)
