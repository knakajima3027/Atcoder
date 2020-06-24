N = int(input())
alpha = [chr(i) for i in range(97, 97+26)]

if N <= 26:
    print(alpha[N-1])
else:
    digit = 1
    tmp = 26
    while True:
        if N <= tmp:
            break
        digit += 1
        tmp += 26 ** digit

    ans = ''
    for i in range(digit):
        ans += alpha[N // (26 ** (digit - i - 1)) - 1]
        N = N - ((N // (26 ** (digit - i - 1))) * (26 ** (digit - i - 1)))

    print(ans)