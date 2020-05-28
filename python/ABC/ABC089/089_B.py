N = int(input())
S = list(map(str, input().split()))
result =  'Three'

for i in range(N):
    if S[i] == 'Y':
        result = 'Four'
        break

print(result)
