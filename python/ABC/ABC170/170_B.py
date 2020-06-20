X, Y = map(int, input().split())

ans = 'No'
for i in range(X + 1):
    bird = i
    turt = X - i

    if 2 * bird + 4 * turt == Y:
        ans = 'Yes'

print(ans)