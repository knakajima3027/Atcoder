s = input()
t = input()
S = []
T = []

for i in range(len(s)):
    S.append(s[i])

for i in range(len(t)):
    T.append(t[i])

S.sort()
T.sort()
T.reverse()

if S == T:
    print('No')

elif min(S, T) == S:
    print('Yes')

else:
    print('No')
