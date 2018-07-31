N = int(input())
arr = [ list(map(int, input().split())) for i in range(N)]
arr.insert(0, [0, 0, 0])
res = 'Yes'

for i in range(N):
    x = arr[i+1][1] - arr[i][1]
    y = arr[i+1][2] - arr[i][2]
    t = arr[i+1][0] - arr[i][0]

    if x+y <= t:
        if (x+y-t)%2 == 0:
            pass
        else:
            res = 'No'
            break
    else:
        res = 'No'
        break

print(res)
        
