X = input()
a = int(X[0])
b = int(X[1])
c = int(X[2])
d = int(X[3])
end = 0
res = a
L = ['+', '-']

for i in L:
    if end == 1:
        break
    for j in L:
        if end == 1:
            break

        for k in L:
            res = a
            if i == '+':
                res += b
            else:
                res -= b

            if j == '+':
                res += c
            else:
                res -= c

            if k == '+':
                res += d
            else:
                res -= d

            if res == 7:
                end = 1
                print(str(a) + i + str(b) + j + str(c) +  str(k) + str(d) + '=7')
                break

            
