import math

A, B, H, M = map(int, input().split())

th_h = 360 // 12 * H + 360 / 12 / 60 * M
th_m = 360 // 60 * M

ans = A ** 2 + B ** 2 - 2*A*B*math.cos(math.radians(abs(th_h - th_m)))
print(math.sqrt(ans))