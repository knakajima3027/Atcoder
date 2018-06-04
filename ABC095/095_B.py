N, X = map(int,input().split())
arr = [int(input()) for j in range(N)]

arr.sort()
X = X - sum(arr)
num = int(X/arr[0])

print(num + len(arr))
