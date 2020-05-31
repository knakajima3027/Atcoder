H1, M1, H2, M2, K = map(int, input().split())

tmp1 = (H2 - H1 - 1) * 60
tmp2 = 60 - M1 + M2
print(tmp1 + tmp2 - K)
