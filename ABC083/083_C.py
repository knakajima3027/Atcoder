A, B = map(int, input().split())
count = 1
for i in range(10**5):
    A = A*2
    if A > B:
        break
    count += 1

print(count) 
