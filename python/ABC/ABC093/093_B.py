A, B, K = map(int, input().split())

if A+K > B:
    for i in range(A, B+1):
        print(i)

else:
    for i in range(A, A+K):
        print(i)

    for j in range(max(i, B-K), B):
        print(j+1)
