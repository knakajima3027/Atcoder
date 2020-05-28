import itertools
N = int(input())
F = [list(map(int, input().split())) for i in range(N)]
P = [list(map(int, input().split())) for i in range(N)]
max_res = -10**9
 
me_list = list(itertools.product([0, 1], repeat=10))
for i in range(1, 2**10):
    res = 0
    co = [ 0 for o in range(N)]
    for j in range(10):
        if me_list[i][j] == 1:
            for k in range(N):
                co[k] += F[k][j]
    for j in range(N):
        res += P[j][co[j]]
    if res > max_res:
        max_res = res
            
print(max_res)
