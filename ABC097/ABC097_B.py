X = int(input())
max1 = 1
max2 = 0

for b in range(1, X+1):
    for q in range(2, X+1):
        if b**q > X:
            break
        max1 = b**q

    if max1 > max2:
        max2 = max1

print(max2)
