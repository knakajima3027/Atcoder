X = int(input())

ans = (X // 500) * 1000
X = X - 500 * (X // 500)
ans += (X // 5) * 5
print(ans)