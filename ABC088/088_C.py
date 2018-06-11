C = [list(map(int, input().split())) for i in range(3)]

a = [0]
b = []
result = 'Yes'

b.append(C[0][0])
b.append(C[0][1])
b.append(C[0][2])
a.append(C[1][0] - b[0])
a.append(C[2][0] - b[0])

for i in range(3):
    for j in range(3):
        if C[i][j] != a[i] + b[j]:
            result = 'No'

print(result)
