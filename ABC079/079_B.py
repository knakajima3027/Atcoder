N = int(input())
a = 2
b = 1

for i in range(N):
    c = a + b
    a = b
    b = c

print(a)
