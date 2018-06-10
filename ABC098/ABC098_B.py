N = int(input())
S = input()

same_num = -1

for i in range(N):
    s1 = set(S[:i+1])
    s2 = set(S[i+1:])
    if len(s1 & s2) > same_num:
        same_num = len(s1 & s2)

print(same_num)
