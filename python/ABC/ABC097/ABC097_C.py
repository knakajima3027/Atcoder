s = input()
K = int(input())
gram_list = []

for i in range(len(s)):
    for j in range(i+1, i+K+1):
        gram_list.append(s[i:j])

gram_list = list(set(gram_list))
gram_list.sort()
print(gram_list[K-1])
