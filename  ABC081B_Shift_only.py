#入力文字数を指定
#一行で空白区切りで数字を入力
#例) 3
#   1 2 3

N = int(input())
A = list(map(int,input().split()))

count = 0

def half(n):
    return n/2

while True:
    if all(elem%2 == 0 for elem in A):
        A = list(map(half, A))
        count += 1
    else:
        break

print(count)
