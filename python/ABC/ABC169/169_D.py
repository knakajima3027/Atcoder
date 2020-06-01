N = int(input())

#nを素因数分解したリストを返す
def prime_factor(n):
    i = 2
    table = []
    while i * i <= n:
        while n % i == 0:
            n //= i
            table.append(i)
        i += 1
    if n > 1:
        table.append(n)
    return table


primes = prime_factor(N)

prime_dic = {}
for i in range(len(primes)):
    if primes[i] in prime_dic:
        prime_dic[primes[i]] += 1
    else:
        prime_dic[primes[i]] = 1

sum_list = [0 for _ in range(30)]
sum_list[0] = 1
for i in range(29):
    sum_list[i+1] += sum_list[i] + (i + 2)

ans = 0
for key in prime_dic:
    for i in range(30):
        if sum_list[i] > prime_dic[key]:
            ans += i
            break

print(ans)