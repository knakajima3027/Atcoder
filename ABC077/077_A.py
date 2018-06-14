l = input()
m = input()
res = 'Yes'


if l[0] != m[2]:
    res = 'No'

if l[1] != m[1]:
    res = 'No'

if l[2] != m[0]:
    res = 'No'

print(res)
