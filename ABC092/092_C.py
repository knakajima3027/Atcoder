N = int(input())
A = list(map(int, input().split()))
A.insert(0, 0)
A.append(0)
distance = []

for i in range(N+1):
    distance.append(abs(A[i+1]-A[i]))


dist_sum = sum(distance)

for i in range(1, N+1):
    result = dist_sum + abs(A[i-1] - A[i+1]) - ( abs(A[i-1] - A[i]) + abs(A[i] - A[i+1]) )
    print(result)
