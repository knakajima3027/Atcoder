N = list(map(int, input().split()))
N.sort()

if (N[1] - N[0])%2 == 0:
    result = int((N[1] - N[0])/2) + N[2] - N[1]

else:
    result = int((N[1] - N[0])/2) + N[2] - N[1] + 2

print(result)
