N = int(input())
a = list(map(int, input().split()))
a.sort()
a.reverse()
result = 0
for i in range(N):
    if i%2 == 0:
        result += a[i]
    else:
        result += -a[i]


print(result)
