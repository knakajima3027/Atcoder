A, B, C, X, Y = map(int, input().split())
yen = 0
if (A+B)/2 > C:
    if X < Y:
        yen += 2*C*X
        yen += min(C*2, B)*(Y - X)
    else:
        yen += 2*C*Y
        yen += min(C*2, A)*(X - Y)

else:
    yen += A*X + B*Y

print(yen)
    
