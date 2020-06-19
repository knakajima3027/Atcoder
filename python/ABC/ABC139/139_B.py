A, B = map(int, input().split())

tmp = 1
ans = 0
while True:
    if tmp >= B:
        print(ans)
        break
    tmp += A - 1
