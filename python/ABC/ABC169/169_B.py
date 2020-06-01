N = int(input())
A = list(map(int, input().split()))

A.sort()
if A[0] == 0:
    print(0)
else:
    ans = 1
    for i in range(N):
        ans *= A[i]
        if ans > 10 ** 18:
            ans = -1
            break

    print(ans)