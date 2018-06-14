X, Y, Z = map(int, input().split())

for i in range(10**5):
    if X - Y*i - Z*i < Y + 2*Z :
        res += 1
        break
    res = i

print(res)
