#解くのに工夫が必要. 'dream'と'dreamer'は先頭から見ていくと被ってしまう.
#逆にしてみると'maerd', 'remaerd'となり被らなくなる!
S = input()
T = ''
t = ''
result = 'YES'
dream_list = ['maerd', 'remaerd', 'esare', 'resare']

for i in range(1, len(S)+1):
    t += S[-i]
    if t in dream_list:
        T += t
        t = ''

    if len(t) >7:
        result = 'NO'
        break

if t != '':
    result = 'NO'

print(result)
