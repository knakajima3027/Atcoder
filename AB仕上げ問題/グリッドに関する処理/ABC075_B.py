W, H=map(int,input().split())
arr = [input() for j in range(W)]
ans = ['' for i in range(W)]

for i in range(0, W):
    for j in range(0, H):
        bomb_num = 0
        if arr[i][j] == '#':
            ans[i] += '#'
        else:
            for k in (-1, 0, 1):
                for l in (-1, 0, 1):
                    if (-1<i+k<W) and (-1<j+l<H):
                        if arr[i+k][j+l] == '#':
                            bomb_num += 1

            ans[i] += str(bomb_num)

for i in range(W):
        print(ans[i])
        
