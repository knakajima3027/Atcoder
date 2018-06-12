a, b = map(str, input().split())

c = int(a + b)
res = 'No'

for i in range(2, c):
    if i**2 == c:
        res = 'Yes'
        break
print(res)
