N = int(input())

tmp = 0
for i in range(len(str(N))):
    tmp += int(str(N)[i])

if N%tmp == 0:
    print('Yes')
else:
    print('No')