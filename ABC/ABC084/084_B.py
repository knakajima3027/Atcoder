A, B = map(int, input().split())
S = input()
res = 'Yes'

for i in range(len(S)):
    if i == A:
        if S[i] != '-':
            res = 'No'
            break
    else:
        if S[i].isdigit() == False:
            res = 'No'

print(res)
