N = int(input())
arr = list(map(int, input().split()))
X = arr.copy()
arr.sort()

for i in range(N):
    if X[i] < arr[int(N/2)]:
        print(arr[int(N/2)])
    else:
        print(arr[int(N/2)-1])
