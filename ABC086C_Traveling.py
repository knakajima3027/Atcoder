#入力: N個のt, x, y のセット
#3
#1 2 3
#3 2 1
#6 3 7

N = int(input())
list_txy = [[0, 0, 0]]
for i in range(N):
    list_txy.append(list(map(int,input().split())))

result = 'Yes'

for i in range(N):
    start = list_txy[i]
    goal = list_txy[i+1]
    dist = abs(goal[1] - start[1]) + abs(goal[2] - start[2])
    time = goal[0] - start[0]
    if dist > time:
        result = 'No'
        break

    if (dist%2 != 1 and time%2 != 0) or (dist%2 != 0 and time%2 != 1):
        result = 'No'


print(result)
