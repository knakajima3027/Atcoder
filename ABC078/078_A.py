A, B = map(str, input().split())

if A == B:
    print('=')
elif max(A, B) == A:
    print('>')

else:
    print('<')
