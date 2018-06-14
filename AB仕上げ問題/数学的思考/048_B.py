a, b, x = map(int, input().split())

def f(n, x):
    if n >= 0:
        return (n//x) + 1
    else:
        return 0

print(f(b, x) - f(a, x))
