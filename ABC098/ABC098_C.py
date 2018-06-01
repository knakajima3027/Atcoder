N = int(input())
S = input()

min_num = 10**7
west_num = [0]
east_num = [0]
w_max = 0
e_max = 0

for i in range(0, N): #累積和を求める.
    if S[i] == 'W':
        w_max += 1
    else:
        e_max += 1

    west_num.append(w_max)
    east_num.append(e_max)

for i in range(0, N):
    num = west_num[i] + east_num[-1] - east_num[i+1]
    if num < min_num:
        min_num = num

print(min_num)
