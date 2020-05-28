A = int(input())
D, X = map(int, input().split())
arr = [int(input()) for i in range(A)]

count = 0

for i in range(A):
    count += int((D-1)/arr[i] + 1)

print(count + X)
