N = input()
count = 0

for i  in N:
    count += int(i)

if int(N)%count == 0:
    print('Yes')
else:
    print('No')
