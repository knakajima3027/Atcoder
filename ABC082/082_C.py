from collections import Counter
N = int(input())
a = list(map(int, input().split()))
L = list(set(a))
res = 0

d = Counter()
d.update(a)

for i in L:
    X = d[i]
    if X < i:
        res += X

    else:
        res += X - i

print(res)
    
