N, A, B = map(int,input().split())
count = 0
for i in range(1, N+1):
    sum = 0
    for j in str(i):
        sum += int(j)
    if  A <=sum <=B:
        count += i

print(count)
