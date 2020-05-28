N = int(input())
s = [input() for i in range(N)]

M = int(input())
t = [input() for i in range(M)]

count_max = 0
for i in range(N):
    count = s.count(s[i]) - t.count(s[i])
    if count > count_max:
         count_max = count

print(count_max)
