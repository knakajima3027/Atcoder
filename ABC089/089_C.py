import itertools
N = int(input())
S = [input() for i in range(N)]
U = []
n = [0,0,0,0,0]
result = 0

for i in range(N):
    if S[i][0] == 'M' or S[i][0] == 'A' or S[i][0] == 'R' or S[i][0] == 'C' or S[i][0] == 'H':
        U.append(S[i][0])

    if S[i][0] == 'M':
        n[0] += 1
    if S[i][0] == 'A':
        n[1] += 1
    if S[i][0] == 'R':
        n[2] += 1
    if S[i][0] == 'C':
        n[3] += 1
    if S[i][0] == 'H':
        n[4] += 1

c = list(itertools.combinations(n,3))

for i in range(10):
    result = result + c[i][0]*c[i][1]*c[i][2]

print(result)
