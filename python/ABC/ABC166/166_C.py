N, M = map(int, input().split())
H = list(map(int, input().split()))
root = [list(map(int, input().split())) for _ in range(M)]

is_min = [0 for _ in range(N)]
for i in range(M):
    A = root[i][0] - 1
    B = root[i][1] - 1

    if H[A] > H[B]:
        is_min[B] = 1

    elif H[A] == H[B]:
        is_min[A] = 1
        is_min[B] = 1

    else:
        is_min[A] = 1

print(N - sum(is_min))