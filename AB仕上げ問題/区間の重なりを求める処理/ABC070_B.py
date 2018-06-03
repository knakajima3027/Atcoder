A, B, C, D = map(int, input().split())

if B < C or D < A:
    print(0)

elif A < C:
    print(min(B - C, D - C))

else:
    print(min(D - A, B - A))
