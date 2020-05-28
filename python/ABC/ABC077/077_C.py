import bisect
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A.sort()
C.sort()
res = 0
for i in B:
    res += bisect.bisect_left(A, i) * (N - bisect.bisect_right(C, i))
    
print(res)
