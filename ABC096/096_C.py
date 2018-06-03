W, H = map(int,input().split())
arr = [input() for j in range(W)]
ans = 'Yes'

for i in range(0, W):
    for j in range(0, H):
        t = 0
        if arr[i][j] == '#':
            for k in (-1, 1):
                if (-1 < i+k < W):
                    if arr[i+k][j] == '#':
                        t = 1
                        break

                if (-1 < j+k < W):
                    if arr[i][j+k] == '#':
                        t = 1
                        break
            if t == 0:
                ans = 'No'
                break

print(ans)
          
