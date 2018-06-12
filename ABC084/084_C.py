N = int(input())
l = [list(map(int, input().split())) for j in range(N-1)]

t = []
for i in range(N):
    t = 0
    for j in range(i, N-1):
        if t < l[j][1]:
            t = l[j][1]

        elif 0 == (t%(l[j][2])):
            pass

        else:
            t += -(t%(l[j][2])) + l[j][2]

        t += l[j][0]

    print(t)
