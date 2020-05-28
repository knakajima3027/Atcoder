X = int(input())

flag = False
for a in range(-20 ** 2, 20 ** 2):
    for b in range(-20 ** 2, 20 ** 2):
        if a ** 5 - b ** 5 == X:
            print(a, b)
            flag = True
            break

    if flag:
        break