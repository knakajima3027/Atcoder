T = list(input())

for i in range(len(T)):
    if T[i] == '?':
        T[i] = 'D'

ans = ''
for i in range(len(T)):
    ans += T[i]

print(ans)
