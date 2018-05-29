N, Y = map(int, input().split())
a, b, c = -1, -1, -1

for i in range(N+1):
    for j in range(N+1-i):
        k = N - i - j
        if (10000*i + 5000*j + 1000*k == Y):
            a, b, c = i, j, k
            break

print("%d %d %d" %(a, b, c))
