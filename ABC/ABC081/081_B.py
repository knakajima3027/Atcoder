N = int(input())
L = list(map(int, input().split()))
count = 0
k = 0
for i in range(15):
    for j in range(N):
        if L[j]%2 == 0:
            L[j] = int(L[j]/2)
        else:
            k = 1
            break
    if k == 1:
        break
    count += 1

print(count)
