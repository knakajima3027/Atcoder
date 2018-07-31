N = int(input())
red = [list(map(int, input().split())) for i in range(N)]
blue = [list(map(int, input().split())) for i in range(N)]
count = 0

for i in range(N): #red
    min_dist = 1000
    for j in range(N): #blue
        if (red[i][0] < blue[j][0]) and (red[i][1] < blue[j][1]):
            dist = blue[j][0] - red[i][0] + blue[j][1] - red[i][1]
            if dist < min_dist:
                min_dist = dist
                tmp = j

    blue[tmp][0] = 10000
    blue[tmp][1] = 10000

    if min_dist != 1000:
        count += 1


print(count)
