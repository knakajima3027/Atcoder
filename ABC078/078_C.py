N, M = map(int, input().split())

n = 2 ** M

print(1900*M*n + 100*(N-M)*n) 
