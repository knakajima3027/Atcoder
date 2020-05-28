N = int(input())

for i in range(N+1):
    n = i*i
    if n > N:
        break

    res = n

print(res)
