from collections import Counter
d = Counter()
N, K = map(int, input().split())
A = list(map(int, input().split()))
L = list(set(A))
res = 0
num = []
d.update(A)
if len(L) <= K:
    res = 0

else:
    for i in L:
        num.append(d[i])

    num.sort()

    for i in range(len(L) - K):
        res += num[i]

print(res)
