N, M, X = map(int, input().split())
arr = input().split()
list_fee = []

for i in range(N):
    if arr == []:
        break
    if int(arr[0]) == i+1:
        list_fee.append(1)
        arr.pop(0)
    else:
        list_fee.append(0)

a = list_fee[:X].count(1)
b = list_fee[X:].count(1)

print(min(a, b))
