N = int(input())
n = 1

for i in range(1, N+1):
    n = (n * i)%(10**9+7)

print(n)
