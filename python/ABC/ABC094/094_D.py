N = int(input())
L = list(map(int, input().split())) 

L.sort()
res1 = L[-1]

tmp = res1 / 2

res2 = 10 ** 10
for i in range(N-1):
    if abs(tmp - L[i]) < abs(tmp - res2):
        res2 = L[i]
    
print(res1, res2)

